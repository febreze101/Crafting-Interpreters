import sys

class Lox:
    # keeps track of if an error has occured during program execution
    hadError = False
    
    @staticmethod
    def main(args):
        if len(args) > 1:
            print("Usage: pLox {script}")
            sys.exit(64)
        elif len(args) == 1:
            Lox.run_file(args[0])
        else:
            Lox.run_prompt()
            
    @staticmethod
    def run_file(path):        
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                Lox.run(content)
                
                # on error, don't execute and exit
                if (Lox.hadError):
                    sys.exit(65)
                
        except Exception as E:
            print(f"Exception occured: {E}")
            sys.exit(65)
    
    @staticmethod
    def run_prompt():
        while True:
            line = input('> ')
            if not line:
                break
            
            Lox.run(line)
            hadError = False
            
            
    @staticmethod
    def run(source):
        """interpret and execute source code"""
        print(f'Executing: {source}')
        
    
    def error(line, message):
        Lox.report(line, "", message)
        
    @staticmethod
    def report(line, where, message):
        sys.stderr.write(f'[line {line}] Error {where}: {message}')
        hadError = True
        
    
            
if __name__ == "__main__":
    Lox.main(sys.argv[1:])