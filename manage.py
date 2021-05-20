from road_service.app import create_app

if __name__ == '__main__':
    app = create_app()
    app.manager.run()
