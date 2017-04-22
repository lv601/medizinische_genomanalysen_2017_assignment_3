#! /usr/bin/env python2

import vcf
from vcf import utils
#import hgvs


__author__ = 'mgollobich'


class Assignment3:
    
    def __init__(self):
        ## Check if pyvcf is installed
        print("PyVCF version: %s" % vcf.VERSION)
        ## Check if hgvs is installed
        #print("HGVS version: %s" % hgvs.__version__)

        # Initialize reader for the three vcf files
        self.vcf_mother = vcf.Reader(open('AmpliseqExome.20141120.NA24143.vcf','r'))
        self.vcf_father = vcf.Reader(open('AmpliseqExome.20141120.NA24149.vcf','r'))
        self.vcf_son = vcf.Reader(open('AmpliseqExome.20141120.NA24385.vcf','r'))

    def get_total_number_of_variants_mother(self):
        self.vcf_mother = vcf.Reader(open('AmpliseqExome.20141120.NA24143.vcf','r'))
        number_mother = 0
        for record in self.vcf_mother:
            number_mother += 1
        return number_mother
        
        
    def get_total_number_of_variants_father(self):
        self.vcf_father = vcf.Reader(open('AmpliseqExome.20141120.NA24149.vcf','r'))
        number_father = 0
        for record in self.vcf_father:
            number_father += 1
        return number_father


       
        
    def get_variants_shared_by_father_and_son(self):
        self.vcf_father = vcf.Reader(open('AmpliseqExome.20141120.NA24149.vcf', 'r'))
        self.vcf_son = vcf.Reader(open('AmpliseqExome.20141120.NA24385.vcf', 'r'))
        records = 0
        for record in self.vcf_father:
            if record in self.vcf_son:
                records += 1
        return records

        
    def get_variants_shared_by_mother_and_son(self):
        self.vcf_mother = vcf.Reader(open('AmpliseqExome.20141120.NA24143.vcf', 'r'))
        self.vcf_son = vcf.Reader(open('AmpliseqExome.20141120.NA24385.vcf', 'r'))
        records = 0
        for record in self.vcf_mother:
            if record in self.vcf_son:
                records += 1
        return records

        
    def get_variants_shared_by_trio(self):
        self.vcf_mother = vcf.Reader(open('AmpliseqExome.20141120.NA24143.vcf', 'r'))
        self.vcf_father = vcf.Reader(open('AmpliseqExome.20141120.NA24143.vcf', 'r'))
        self.vcf_son = vcf.Reader(open('AmpliseqExome.20141120.NA24385.vcf', 'r'))
        records = 0
        for record in self.vcf_mother:
            if record in self.vcf_father and record in self.vcf_son:
                records += 1
        return records
        

    def merge_mother_father_son_into_one_vcf(self):
        self.vcf_mother = vcf.Reader(open('AmpliseqExome.20141120.NA24143.vcf', 'r'))
        self.vcf_father = vcf.Reader(open('AmpliseqExome.20141120.NA24143.vcf', 'r'))
        self.vcf_son = vcf.Reader(open('AmpliseqExome.20141120.NA24385.vcf', 'r'))
        merge_file = open("merge_file.vcf", "w")
        writer = vcf.Writer(merge_file, self.vcf_mother, "\n")
        for records in utils.walk_together(self.vcf_mother, self.vcf_father, self.vcf_son):
            for entry in records:
                if entry is not None:
                    writer.write_record(entry)
        print("merge VCF successfull")
        
    def convert_first_variants_of_son_into_HGVS(self):
        return NONE
    
    def print_summary(self):
        print("Print all results here")
        print('{:<8}'.format(self.get_total_number_of_variants_mother()),"Variants of Mother")
        print('{:<8}'.format(self.get_total_number_of_variants_father()),"Variants of Father")
        print('{:<8}'.format(self.get_variants_shared_by_father_and_son()),"Variants shared by Father and Son")
        print('{:<8}'.format(self.get_variants_shared_by_mother_and_son()),"Variants shared by Mother and Son")
        print('{:<8}'.format(self.get_variants_shared_by_trio()),"Variants shared by Trio")
        print(self.merge_mother_father_son_into_one_vcf())
        
if __name__ == '__main__':
    print("Assignment 3")
    assignment1 = Assignment3()
    assignment1.print_summary()
    
    

