import click

@click.command()
@click.option('--name') 
@click.option('--password', prompt = True, hide_input = True)

def main(name, password):

    fname = click.prompt('FirstName : ')
    click.echo(f'Name: {name}\n FirstName: {fname}\n Password: {password}')

if __name__== '__main__':
    main()
