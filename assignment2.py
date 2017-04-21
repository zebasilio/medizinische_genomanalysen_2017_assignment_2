#! /usr/bin/env python3

'''
Before running the script, change the path of the vcf file in the file variable (line 16)
to run the script, in the command line:
$chmod +x assignment2.py
$./assignment2.py > assignment2.txt
'''



import vcf

__author__ = 'José Basílio'

file = "/home/jose/MedGenAn/medizinische_genomanalysen_2017_assignment_2/AmpliseqExome.20141120.NA24385.vcf"


class Assignment2:
    
    def __init__(self):
        ## Check if pyvcf is installed
        print("PyVCF version: %s" % vcf.VERSION)
        

    def get_average_quality_of_son(self):
        
        print("\n+++++++++++++++++++\nGet the average PHRED quality of all son variants:")
        sum = 0
        count = 0
        for line in vcf.Reader(open(file, "r")):
            sum = sum + line.QUAL
            count += 1
        average_quality_of_son = sum / count
        print("%.2f" % round(average_quality_of_son,2))
        return average_quality_of_son
    
        
    def get_total_number_of_variants_of_son(self):
        print("\n+++++++++++++++++++\nGet the total number of son variants:")
        total_number_variants = 0
        for line in vcf.Reader(open(file, "r")):
            total_number_variants += 1
        print(total_number_variants)
        return total_number_variants
    
    
    
    def get_variant_caller_of_vcf(self):
        print("\n+++++++++++++++++++\nReturn the variant caller name:")
        for line in vcf.Reader(open(file, "r"))._header_lines:
            if line.startswith("##source"):
                print("-", str.split(line, '"')[1])
                return "-", str.split(line, '"')[1]

    def get_human_reference_version(self):
        print("\n+++++++++++++++++++\nReturn the genome reference version:")
        for line in vcf.Reader(open(file, "r"))._header_lines:
            if line.startswith("##reference=file://"):
                print(str.split(line, '/')[6])
                return str.split(line, '/')[6]

    def get_number_of_indels(self):
        print("\n+++++++++++++++++++\nReturn the number of identified INDELs:")
        count = 0
        for line in vcf.Reader(open(file, "r")):
            if line.is_indel:
                count += 1
        print(count)
        return count
       
       
    def get_number_of_snvs(self):
       print("\n+++++++++++++++++++\nReturn the number of SNVs:")
       count = 0
       for line in vcf.Reader(open(file, "r")):
            if line.is_snp:
                count += 1
       print(count)
       return count
        
    def get_number_of_heterozygous_variants(self):
       print("\n+++++++++++++++++++\nReturn the number of heterozygous variants:")
       count = 0
       for line in vcf.Reader(open(file, "r")):
           count += line.num_het
       print(count)
       return count

    
    def print_summary(self):
        self.get_average_quality_of_son()
        self.get_total_number_of_variants_of_son()
        self.get_variant_caller_of_vcf()
        self.get_human_reference_version()
        self.get_number_of_indels()
        self.get_number_of_snvs()
        self.get_number_of_heterozygous_variants()
    
        
if __name__ == '__main__':
    print("Assignment 2")
    assignment1 = Assignment2()
    assignment1.print_summary()
    
    

