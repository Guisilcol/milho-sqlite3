import traceback
import arguments
import commands
from warnings import filterwarnings
import sys

def main():
    try:
        args = arguments.get_arg_parse()

        if not args.get("is_dev"):
            filterwarnings("ignore")
        
        if args.get("is_dev"):
            print(args)
        
        command = args.get("command")

        if(command == "load"):
            commands.Load.run(commands.LoadArgs(**dict(args)))
        elif(command == "execute"):
            commands.Execute.run(commands.ExecuteArgs(**dict(args)))
        elif(command == "use"):
            commands.Use.run(commands.UseArgs(**dict(args)))
        elif(command == "index"):
            commands.Index.run(commands.IndexArgs(**dict(args)))
        elif(command == "export"):
            commands.Export.run(commands.ExportArgs(**dict(args)))
        elif(command == "fixedcolswidth"):
            commands.FixedColsWidth.run(commands.FixedColsWidthArgs(**dict(args)))
        else:
            print("> Comando não implementado")

        sys.exit(0)
        
    except Exception as error:
        print("> Ocorreu um erro: ", '\n\n', traceback.format_exc())
        sys.exit(1)

if __name__ == "__main__":
    main()