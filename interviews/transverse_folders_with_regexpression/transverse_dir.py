import os, sys
import re

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

__author__ = "Renato Maschion"
__Project__ = "screening exercise"

class TransverseDir():
    """
    Searches files recursively for a keyword in a form of regular expression pattern
    example: "LogFile" -> will return the number of word "logFile" found on each file
             in the path.
             "^[a-zA-Z]+_TESTResult.*  -> will return one hit for each file starting with
             a word starting for an alphabetical char and immediatelly followed by a "_" and
             the work TESTResul

    File type: any file type can be searched. No requirement for file type

    Arguments:
        root_dir: the initial file path position to start the search
        keyword:  a valid regular expression to use during the search

    Output:
        An output array of all the data, for example {'a/b': 6, 'a/b/c': 7, '/a/b/c/d':0}
        An output graph with a plot with X as subdir name string, Y as count values
    """
    compiled_exp = object

    def __init__(self, root_dir):
        self.results = {}
        self.root_dir = root_dir
        head, _ = os.path.split(self.root_dir)
        os.chdir(head)

    def compile_regular_expression(self, regular_expression):
        self.regular_expression = regular_expression
        try:
            self.compiled_exp = re.compile(self.regular_expression)
        except Exception, e:
            raise Exception("Bad Regular Expression. ERROR: %s" % e.message)

    def search_expression(self, current_dir, files):
        try:
            for f in files:
                # count how many times regular expression is true in the file
                count = 0
                with open(current_dir+os.sep+f) as file:
                    if f[0] in '__ .': continue
                    contents = file.read().strip()
                    count = len(self.compiled_exp.findall(contents))
                    yield f, count
        except Exception, e:
            raise Exception("Error detected during Search Expression. ERROR: %s" % e.message )

    def walkdir(self):
        try:
            #loop all childreen directories
            for cur, _dirs, files in os.walk(self.root_dir):
                #split current diretory in root/tail
                head, tail = os.path.split(cur)
                #iterate files in child
                file_count = self.search_expression(cur, files)
                [self.results.update({r"%s/%s" % (head+"/"+tail,filename):count}) for filename, count in file_count]
        except Exception, e:
            raise e

    def print_results(self, pref = ''):
        try:
            print self.results
            for key in self.results:
                print("{0:<50}{1:10}".format(key,self.results[key]))
        except Exception, e:
            raise e

    def plot_results(self):
        try:
            plt.rcdefaults()

            objects  = self.results.keys()
            y_values = self.results.values()
            y_pos    = np.arange(len(objects))

            plt.bar(y_pos, y_values, align='center', alpha=0.5)
            plt.xticks(y_pos, objects)
            plt.xlabel('word hits')
            plt.title('Number Regular Expression Found')
            plot_margin = 0.2
            plt.gcf().subplots_adjust(bottom=0.50)
            x0, x1, y0, y1 = plt.axis()
            plt.axis((x0 - plot_margin,
                      x1 + plot_margin,
                      y0 + plot_margin,
                      y1 + plot_margin))
            plt.xticks(rotation=90)
            plt.show()
        except Exception, e:
            raise e

    def get_results_list(self):
        return self.results

if __name__ == '__main__':
    transverse = TransverseDir("./test")
    transverse.compile_regular_expression('Logfile')
    transverse.walkdir()
    transverse.print_results()
    transverse.plot_results()


