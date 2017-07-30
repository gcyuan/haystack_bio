import os
import sys
import urllib2
import shutil as sh
from bioutilities import Genome_2bit
from haystack_common import determine_path, query_yes_no

HAYSTACK_VERSION = "0.5.0"

def download_genome(name, answer):
    if answer== "--yes" or query_yes_no('Should I download it for you?'):
        output_directory= determine_path('genomes')
        print 'genome_directory: %s' % output_directory
        try:
            urlpath = "http://hgdownload.cse.ucsc.edu/goldenPath/%s/bigZips/%s.2bit" % (name, name)
            genome_url_origin = urllib2.urlopen(urlpath)
            genome_filename = os.path.join(output_directory, "%s.2bit" % name)
            if os.path.exists(genome_filename):
                print 'File %s exists, skipping download' % genome_filename
            else:
                print 'Downloding %s in %s...' % (urlpath, genome_filename)
                with open(genome_filename, 'wb') as genome_file_destination:
                    sh.copyfileobj(genome_url_origin, genome_file_destination)

                print 'Downloaded %s in %s:' % (urlpath, genome_filename)

        except IOError, e:
                print "Can't retrieve %r to %r: %s" % (urlpath, genome_filename, e)
                return
        g = Genome_2bit(genome_filename, verbose=True)

        chr_len_filename = os.path.join(output_directory, "%s_chr_lengths.txt" % name)
        if not os.path.exists(chr_len_filename):
            print 'Extracting chromosome lengths'
            g.write_chr_len(chr_len_filename)
            print 'Done!'
        else:
            print 'File %s exists, skipping generation' % chr_len_filename

        meme_bg_filename = os.path.join(output_directory, "%s_meme_bg" % name)
        if not os.path.exists(meme_bg_filename):
            print 'Calculating nucleotide frequencies....'
            g.write_meme_background(meme_bg_filename)
            print 'Done!'
        else:
            print 'File %s exists, skipping generation' % meme_bg_filename
    else:
        print('Sorry I need the genome file to perform the analysis. Exiting...')
        sys.exit(1)

def main():
    print '\n[H A Y S T A C K   G E N O M E   D O W L O A D E R]\n'
    print 'Version %s\n' % HAYSTACK_VERSION
    if len(sys.argv) == 1:
        sys.exit('Example: haystack_download_genome hg19\n')
    elif len(sys.argv) == 2:
        download_genome(sys.argv[1], answer='')
    elif len(sys.argv) == 3:
        download_genome(sys.argv[1], sys.argv[2])
    else:
        sys.exit('Too many arguments')