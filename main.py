from website import create_app

app = create_app()

# Implies that the module is being run standalone by the user and we can do coressponding appropriate actions.
if __name__ =='__main__':
    app.run(debug=True)