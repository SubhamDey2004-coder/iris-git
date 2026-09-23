def test_app_import():
    from src.app import main
    
    assert callable(main)