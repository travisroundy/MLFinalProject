import csv

outfile = open('300k.vw', 'w')
count_file = open('pokemon_summary.csv', 'w')

pokemon_counts = [0] * 151
with open("300k.csv") as infile:
    first=True
    for row in csv.reader(infile):
        if(first == True):
            first=False
            headers = row
        else:
            pokemon_counts[int(row[0])]+=1
            params_string = ""
            for i in range(1,len(row)):
                params_string+=("{}:{} ".format(headers[i], row[i]))

            write_string = "{} | {} \n".format(row[0], params_string)
            outfile.write(write_string)
count_file.write(str(pokemon_counts[1:-2]))
outfile.close()


