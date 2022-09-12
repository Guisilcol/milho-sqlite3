import Arguments
import commands.Load
import commands.Execute
import commands.Use
import commands.Index
import commands.Export
from warnings import filterwarnings

def main():
    args = Arguments.get_arg_parse().parse_args()
    
    if not args.is_dev:
        filterwarnings("ignore")

    if(args.command == "load"):
        commands.Load.run(args)
    elif(args.command == 'execute'):
        commands.Execute.run(args)
    elif(args.command == 'use'):
        commands.Use.run(args)
    elif(args.command == 'index'):
        commands.Index.run(args)
    elif(args.command == 'export'):
        commands.Export.run(args)
    else:
        print("> Comando não implementado")

if __name__ == '__main__':
    main()