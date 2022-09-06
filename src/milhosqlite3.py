import Arguments
import commands.Load
import commands.Execute
import commands.Use
import warnings

def main():
    args = Arguments.get_arg_parse().parse_args()
    
    if not args.is_dev:
        warnings.filterwarnings("ignore")

    if(args.command == "load"):
        commands.Load.run(args)
    if(args.command == 'execute'):
        commands.Execute.run(args)
    if(args.command == 'use'):
        commands.Use.run(args)
    else:
        print("> Comando não implementado")

if __name__ == '__main__':
    main()