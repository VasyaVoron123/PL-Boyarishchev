input_file = 'БоярищевАлександрНиколаевич_У=244_vvod.txt'
output_file = 'БоярищевАлександрНиколаевич_У=244_vivod.txt'
with open(input_file, 'r') as f:
    lines = f.readlines()
processed_lines = lines[::-1]
with open(output_file, 'w') as f:
    f.writelines(processed_lines)