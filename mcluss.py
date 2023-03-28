def qm_algorithm(inputs, outputs):
    minterms = get_minterms(inputs, outputs)
    prime_implicants = get_prime_implicants(minterms)
    chart = get_prime_implicant_chart(prime_implicants, minterms)
    essential_prime_implicants = get_essential_prime_implicants(chart)
    if not essential_prime_implicants:
        return None
    min_terms = get_minimal_terms(essential_prime_implicants, minterms)
    return min_terms

def get_minterms(inputs, outputs):
    minterms = []
    for i in range(len(inputs)):
        if outputs[i]:
            minterms.append(inputs[i])
    return minterms

def get_prime_implicants(minterms):
    prime_implicants = []
    implicant_dict = {}
    for minterm in minterms:
        implicant_dict[minterm] = get_binary_string(minterm)
    while implicant_dict:
        new_dict = {}
        for key1 in implicant_dict:
            for key2 in implicant_dict:
                if key2 > key1:
                    diff_bits = get_diff_bits(implicant_dict[key1], implicant_dict[key2])
                    if len(diff_bits) == 1:
                        new_implicant = implicant_dict[key1][:diff_bits[0]] + "-" + implicant_dict[key1][diff_bits[0] + 1:]
                        if new_implicant not in new_dict.values():
                            new_dict[key1 + key2] = new_implicant
        for key in implicant_dict:
            if key not in new_dict:
                prime_implicants.append(implicant_dict[key])
        implicant_dict = new_dict
    return prime_implicants

def get_binary_string(num):
    binary_string = bin(num)[2:]
    num_bits = len(binary_string)
    padding = "0" * (len(bin(max(inputs))) - num_bits)
    return padding + binary_string

def get_diff_bits(str1, str2):
    diff_bits = []
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            diff_bits.append(i)
    return diff_bits

def get_prime_implicant_chart(prime_implicants, minterms):
    chart = {}
    for implicant in prime_implicants:
        chart[implicant] = []
        for minterm in minterms:
            if is_covered_by_implicant(minterm, implicant):
                chart[implicant].append(minterm)
    return chart

def is_covered_by_implicant(minterm, implicant):
    for i in range(len(implicant)):
        if implicant[i] == "-":
            continue
        if minterm[i] != implicant[i]:
            return False
    return True

def get_essential_prime_implicants(chart):
    essential_implicants = []
    covered_minterms = set()
    for minterm in chart.values():
        if len(minterm) == 1:
            implicant = get_implicant_for_minterm(minterm[0], chart)
            essential_implicants.append(implicant)
            covered_minterms.update(chart[implicant])
    remaining_chart = {}
    for implicant in chart:
        if implicant not in essential_implicants:
            remaining_chart[implicant] = chart[implicant]
    while remaining_chart:
        max_implicant = get_maximal_implicant(remaining_chart)
        essential_implicants.append(max_implicant)
        covered_minterms.update(remaining_chart[max_implicant])
        remaining_chart = get_reduced_chart(remaining_chart, max_implicant)
        for minterm in chart.values():
            if set(minterm).issubset(covered_minterms):
                return essential_implicants
    return essential_implicants


def get_implicant_for_minterm(minterm, chart):
    for implicant, minterms in chart.items():
        if minterm in minterms:
            return implicant


def get_maximal_implicant(chart):
    max_implicant = None
    max_coverage = 0
    for implicant, minterms in chart.items():
        if len(minterms) > max_coverage:
            max_implicant = implicant
            max_coverage = len(minterms)
    return max_implicant


def get_reduced_chart(chart, implicant):
    reduced_chart = {}
    for implicant2, minterms in chart.items():
        if implicant2 != implicant:
            new_minterms = [minterm for minterm in minterms if minterm not in chart[implicant]]
            reduced_chart[implicant2] = new_minterms
    return reduced_chart


def get_minimal_terms(essential_prime_implicants, minterms):
    minimal_terms = set()
    for implicant in essential_prime_implicants:
        for minterm in minterms:
            if is_covered_by_implicant(minterm, implicant):
                minimal_terms.add(minterm)
    return sorted(minimal_terms)


def main():
    num_variables = int(input("Enter the number of variables: "))
    minterms = list(map(int, input("Enter the minterms (comma-separated): ").split(",")))
    dont_cares = []
    response = input("Are there any don't cares? (y/n): ")
    if response == "y":
        dont_cares = list(map(int, input("Enter the don't cares (comma-separated): ").split(",")))

    chart = generate_prime_implicant_chart(num_variables, minterms, dont_cares)
    prime_implicants = get_prime_implicants(chart)
    essential_implicants = get_essential_prime_implicants(chart)

    print("Prime Implicants:")
    print(prime_implicants)
    print("Essential Prime Implicants:")
    print(essential_implicants)
    print("Minimal Expression:")
    print(get_minimal_expression(essential_implicants, num_variables))

if __name__ == "__main__":
    main()

