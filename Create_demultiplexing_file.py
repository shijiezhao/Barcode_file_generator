FL = {}
RL = {}

f = 1
with open('Flist') as g:
	lines = g.readlines()
	for line in lines:
		f_bc = line[:-1]
		FL[f] = f_bc
		f +=1

r = 1
with open('Rlist') as g:
	lines = g.readlines()
	for line in lines:
		r_bc = line[:-1]
		RL[r] = r_bc
		r +=1

import string
tab = string.maketrans("ACTG", "TGAC")

def reverse_complement(seq):
    return seq.translate(tab)[::-1]

ROWS = 'ABCDEFGH'
def write_plate(plate_id,f1,f2,r1,r2,filename1,filename2):
	row = -1
	for fl in range(f1,f2+1):
		row += 1
		col = 0
		for rl  in range(r1,r2+1):
			col += 1
			filename1.write('N7F')
			if fl <10:
				filename1.write('0'+str(fl))
			else:
				filename1.write(str(fl))
			filename1.write('S5R')
			if rl <10:
				filename1.write('0'+str(rl))
			else:
				filename1.write(str(rl))
			filename1.write('_'+plate_id+'_'+ROWS[row]+str(col)+',')
			filename1.write(reverse_complement(FL[fl])+','+RL[rl]+'\n')
			filename2.write('sbatch raw_fastq_processing.slurm '+plate_id+'_'+ROWS[row]+str(col)+' ')
			filename2.write(reverse_complement(FL[fl])+'_'+RL[rl]+'\n')

filename1 = open('Aug_2020.csv','w')
filename2 = open('Aug_2020_processing.slurm','w')

filename1.write('SampleName'+','+'IndexBarcode1'+','+'IndexBarcode2'+'\n')

write_plate('LAC-01',1,8,17,28,filename1,filename2)
write_plate('LAC-02',1,8,29,40,filename1,filename2)
write_plate('LAC-04',1,8,49,60,filename1,filename2)
write_plate('LAC-07',1,8,61,72,filename1,filename2)

write_plate('LAC-08',25,32,49,60,filename1,filename2)
write_plate('LAC-03',25,32,61,72,filename1,filename2)

write_plate('BL-01',33,40,17,28,filename1,filename2)
write_plate('GA-13',33,40,29,40,filename1,filename2)

write_plate('X03',41,48,25,36,filename1,filename2)
write_plate('X02',41,48,37,48,filename1,filename2)
write_plate('BA-01-new',49,56,25,36,filename1,filename2)

write_plate('LAC-05',57,64,1,12,filename1,filename2)
write_plate('LAC-10',57,64,13,24,filename1,filename2)
write_plate('LAC-09',65,72,1,12,filename1,filename2)
write_plate('GA-104',65,72,13,24,filename1,filename2)

write_plate('X04',57,64,49,60,filename1,filename2)
write_plate('BA-01',57,64,61,72,filename1,filename2)
write_plate('PD-03',65,72,49,60,filename1,filename2)
write_plate('LAC-06',65,72,61,72,filename1,filename2)


write_plate('TEST-01',61,64,33,36,filename1,filename2)
write_plate('TEST-02',33,36,45,48,filename1,filename2)
write_plate('TEST-03',17,20,41,44,filename1,filename2)
write_plate('TEST-04',17,20,29,32,filename1,filename2)
write_plate('TEST-05',41,44,5,8,filename1,filename2)
write_plate('TEST-06',9,12,45,48,filename1,filename2)