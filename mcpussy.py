def generate_implicants(minterms, num_variables):
    implicants = []
    for minterm in minterms:
        implicant = format(minterm, f'0{num_variables}b')
        implicants.append(implicant)
    return implicants

def group_implicants_by_num_ones(implicants):
    groups = {}
    for implicant in implicants:
        num_ones = implicant.count('1')
        if num_ones in groups:
            groups[num_ones].append(implicant)
        else:
            groups[num_ones] = [implicant]
    return groups

def get_next_group(grouped_implicants):
    next_group = {}
    for num_ones, implicants in grouped_implicants.items():
        if num_ones + 1 in grouped_implicants:
            next_implicants = generate_combined_implicants(implicants, grouped_implicants[num_ones + 1])
            next_group[num_ones] = list(set(next_implicants))
    return next_group

def generate_combined_implicants(implicants1, implicants2=[]):
    combined_implicants = []
    for implicant1 in implicants1:
        for implicant2 in implicants2:
            combined_implicant = ''
            for i in range(len(implicant1)):
                if implicant1[i] == implicant2[i]:
                    combined_implicant += implicant1[i]
                else:
                    combined_implicant += '-'
            if combined_implicant.count('-') == 1:
                combined_implicants.append(combined_implicant)
    return combined_implicants

def generate_prime_implicant_chart(num_variables, minterms, dont_cares=[]):
    chart = {}
    minterms = set(minterms + dont_cares)

    # Step 1: Generate the initial list of implicants
    implicants = generate_implicants(minterms, num_variables)

    # Step 2: Group the implicants by number of ones
    grouped_implicants = group_implicants_by_num_ones(implicants)

    # Step 3: Generate the prime implicant chart
    while grouped_implicants:
        for num_ones, implicants in grouped_implicants.items():
            for implicant in implicants:
                if implicant in chart:
                    chart[implicant].append(num_ones)
                else:
                    chart[implicant] = [num_ones]
        grouped_implicants = get_next_group(grouped_implicants)
    
    return chart

def get_prime_implicants(chart):
    prime_implicants = []
    for implicant, num_ones in chart.items():
        if len(num_ones) == 1:
            prime_implicants.append(implicant)
    return prime_implicants

def get_essential_prime_implicants(chart):
    essential_implicants = []
    covered_minterms = set()
    num_ones = min([min(num_ones) for num_ones in chart.values()])
    for implicant, minterms in chart.items():
        if num_ones in minterms:
            essential_implicants.append(implicant)
            covered_minterms.update(minterms)
    while covered_minterms != set(chart.values()):
        num_ones += 1
        implicants = [implicant for implicant, minterms in chart.items() if num_ones in minterms]
        for implicant in implicants:
            minterms = set(chart[implicant])
            if minterms - covered_minterms == set():
                essential_implicants.append(implicant)
                covered_minterms.update(minterms)


def generate_prime_implicant_chart(num_variables, minterms, dont_cares=[]):
    chart = {}
    minterms = set(minterms + dont_cares)

    # Step 1: Generate the initial list of implicants
    implicants = generate_implicants(minterms, num_variables)

    # Step 2: Group the implicants by number of ones
    grouped_implicants = group_implicants_by_num_ones(implicants)

    # Step 3: Generate the prime implicant chart
    while grouped_implicants:
        chart.update(grouped_implicants)
        implicants = generate_combined_implicants(grouped_implicants)
        grouped_implicants = group_implicants_by_num_ones(implicants)
    
    return chart

def main():
    num_variables = 4
    minterms = [0, 1, 2, 5, 7, 8, 9, 10, 11, 13, 15]
    dont_cares = [3, 4, 12, 14]

    minimal_expression, essential_implicants, prime_implicants = quine_mccluskey(num_variables, minterms, dont_cares)

    print("Minterms:", minterms)
    print("Don't cares:", dont_cares)
    print("Prime Implicants:")
    for implicant in prime_implicants:
        print(implicant)
    print("Essential Prime Implicants:")
    for implicant in essential_implicants:
        print(implicant)
    print("Minimal Expression:", minimal_expression)

if __name__ == "__main__":
    main()

