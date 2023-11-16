import click
import random
from pizza_class import Margherita, Pepperoni, Hawaiian


@click.group()
def cli():
    """
    Command-line interface for pizza ordering and menu display.
    """
    pass


@cli.command()
@click.argument('pizza_type')
@click.option('--delivery',
              is_flag=True, help='Specify if delivery is required')
def order(pizza_type: str, delivery: bool):
    """
    Place an order for a pizza.

    Args:
        pizza_type : The type of pizza to order.
            Must be one of 'Margherita', 'Pepperoni', or 'Hawaiian'.
        delivery : True if delivery is required, False otherwise.
    """
    if pizza_type not in ['Margherita', 'Pepperoni', 'Hawaiian']:
        click.echo('😔 Sorry, it is not available on the menu.')
        return

    preparation_time = random.randint(1, 30)

    if preparation_time > 15:
        click.echo('😢 Oh no, the pizza '
                   'is taking longer than expected to prepare...')
    else:
        click.echo("😄 Yay! The pizza is being prepared. It'll be ready soon!")

    click.echo(f'🍕 Prepared in {preparation_time}s!')

    if delivery:
        delivery_time = random.randint(1, 30)

        if delivery_time > 15:
            click.echo('😢 Oops, the pizza delivery '
                       'is taking longer than expected...')
        else:
            click.echo('🚴‍♂️ Great news! The pizza is on its way!')

        click.echo(f'🛵 Delivered in {delivery_time}s!')


@cli.command()
def menu():
    """
    Display the pizza menu.
    """
    margherita = Margherita('L')
    pepperoni = Pepperoni('L')
    hawaiian = Hawaiian('L')

    click.echo('Menu:')
    click.echo(f'- 🍅 Margherita : {", ".join(margherita.ingredients)}')
    click.echo(f'- 🍖 Pepperoni : {", ".join(pepperoni.ingredients)}')
    click.echo(f'- 🍍 Hawaiian : {", ".join(hawaiian.ingredients)}')


if __name__ == '__main__':
    cli()
