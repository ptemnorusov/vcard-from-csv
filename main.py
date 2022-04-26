import os

os.makedirs('vcards', exist_ok=True)

with open('vcards.csv', 'r') as vc:
    while True:
        line = vc.readline()
        if line:
            firstname = line.split(';')[0]
            lastname = line.split(';')[2]
            otchestvo = line.split(';')[1]
            companyname = line.split(';')[3]
            position = line.split(';')[4]
            phonenumber = line.split(';')[5]
            website = line.split(';')[6]
            email = line.split(';')[7]
            keepas = line.split(';')[8]

            filename = "vcards/" + line.split(';')[2] + '.vcf'
            with open(filename, 'w', encoding='utf-8') as vcf:
                vcf.write("BEGIN:VCARD\n")
                vcf.write("VERSION:3.0\n")
                vcf.write(f"FN;CHARSET=utf-8:{firstname} {otchestvo} {lastname}\n")
                vcf.write(f"N;CHARSET=utf-8:{lastname};{firstname};{otchestvo};;\n")
                vcf.write(f"EMAIL;CHARSET=utf-8;type=WORK,INTERNET:{email}\n")
                vcf.write(f"TEL;TYPE=work:{phonenumber}\n")
                vcf.write(f"TITLE;CHARSET=utf-8:{position}\n")
                vcf.write(f"ORG;CHARSET=utf-8:{companyname}\n")
                vcf.write(f"URL;type=WORK;CHARSET=utf-8:{website}\n")
                vcf.write(f"END:VCARD")
        else:
            break
