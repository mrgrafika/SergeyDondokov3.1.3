
def test_iteration1(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: 'chicken')
    import ComboMenuv1
    captured = capsys.readouterr() 
   
    assert "chicken" in captured.out

def test_iteration2(monkeypatch, capsys):

    # Simulate multiple user inputs
    inputs = iter(['chicken', 'yes', 'medium'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    # Import and execute the target module
    import ComboMenuv2
    
    # Capture the output
    captured = capsys.readouterr()
    
    # Assert that the output contains the expected sequence of responses
   # print(captured.out)
    assert "$7" in captured.out
    


def test_iteration3v1(monkeypatch, capsys):
    # Simulate multiple user inputs
    inputs = iter(['chicken', 'yes', 'medium', 'yes', 'small','yes'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    # Import and execute the target module
    import ComboMenuv3
    
    # Capture the output
    captured = capsys.readouterr()
    
    # Assert that the output contains the expected sequence of responses
    assert "$9" in captured.out

def test_iteration3v2(monkeypatch, capsys):
    # Simulate multiple user inputs
    inputs = iter(['chicken', 'yes', 'medium', 'no'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    # Import and execute the target module
    import ComboMenuv3
    
    # Capture the output
    captured = capsys.readouterr()
    
    # Assert that the output contains the expected sequence of responses
    assert "fries" in captured.out

def test_iteration3v3(monkeypatch, capsys):
    # Simulate multiple user inputs
    inputs = iter(['chicken', 'yes', 'medium', 'yes', 'small','no'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    # Import and execute the target module
    import ComboMenuv3
    
    # Capture the output
    captured = capsys.readouterr()
    
    # Assert that the output contains the expected sequence of responses
    assert "$8" in captured.out

def test_iteration4(monkeypatch, capsys):
    inputs = inputs = iter(['chicken', 'yes', 'medium', 'yes', 'small','no','5'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    import ComboMenuv4

    captured = capsys.readouterr()
    assert "$9.25" in captured.out
