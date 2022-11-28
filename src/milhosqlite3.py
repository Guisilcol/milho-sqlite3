import arguments
import commands
from warnings import filterwarnings
import sys

def main():
    try:
        args = arguments.get_arg_parse()

        if not args.get("is_dev"):
            filterwarnings("ignore")
        
        if(args.get("command") == "load"):
            commands.Load.run(commands.LoadCommandArgs(**dict(args)))
        elif(args.get("command") == "execute"):
            commands.Execute.run(commands.ExecuteCommandArgs(**dict(args.__dict__)))
        elif(args.get("command") == "use"):
            commands.Use.run(commands.UseCommandArgs(**dict(args)))
        elif(args.get("command") == "index"):
            commands.Index.run(commands.IndexCommandArgs(**dict(args)))
        elif(args.get("command") == "export"):
            commands.Export.run(commands.ExportCommandArgs(**dict(args)))
        else:
            print("> Comando não implementado")

        sys.exit(0)
        
    except Exception as error:
        print("> Ocorreu um erro: ", '\n\n', error)
        sys.exit(1)

if __name__ == "__main__":
    main()