import sys
import webapp2
import psutil
import json
from paste import httpserver


class Cpu_usage(webapp2.RequestHandler):
    def get(self):
        processes = self.get_processList(0.1)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(processes))

    def get_processList(self, seconds=0.1):
        try:
            retval = dict()
            processes = psutil.pids()
            for p in processes[0:298]:  #cannot handle more than 300
                p = psutil.Process(p)
                p.as_dict()
                try:
                    # fix for mac, the bottom was tested on ubuntu
                    if not "Too big to print" in p.name.im_self._name:
                        retval[p.name.im_self._pid] = p.name.im_self._name
                    #else:
                        #pass
                        # this methods doesn't handle too many processes
                        # retval[p.name] = p.get_cpu_percent(interval=seconds)
                except Exception, e:
                    print e  # mac won't allow access to system process and I am not tracking those right now
        except Exception, e:
            print e
            pass  # error handling //TODO
        finally:
            return retval


def main():
    if len(sys.argv) < 3:
        print 'Usage: python cpu_usage.py <URL> <port>'
        print 'Where: URL and Port from the server to listen'

    app = webapp2.WSGIApplication([
        ('/', Cpu_usage), ],
        debug=True)

    httpserver.serve(app, host=sys.argv[1], port=sys.argv[2])


if __name__ == '__main__':
    main()
