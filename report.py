def get_description():
    """Retrun random weather, just like thr pros"""
    from random import choice
    possibilites = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return choice(possibilites)
    
