def brew_chai(flavor):
    if flavor not in ["masala", 'ginger', 'cardamom']:
        raise ValueError('unsupported  chai')
    print(f'Brewing {flavor} chai')
    
brew_chai('mint')