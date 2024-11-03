import Lab_2

def test_find_min_max():
    # Test with a sample list of numbers
    temp_list = [30, 40, 20, 50]
    result = Lab_2.find_min_max(temp_list)
    assert result == [20, 50]

    # Test with all equal values
    temp_list = [30, 30, 30]
    result = Lab_2.find_min_max(temp_list)
    assert result == [30, 30]

    # Test with a single value
    temp_list = [25]
    result = Lab_2.find_min_max(temp_list)
    assert result == [25, 25]

def test_calc_average():
    # Test with a sample list of numbers
    temp_list = [30, 40, 20, 50]
    result = Lab_2.calc_average(temp_list)
    assert result == 35.0

    # Test with a single value
    temp_list = [25]
    result = Lab_2.calc_average(temp_list)
    assert result == 25.0

def test_calc_median_temp():
    # Test with an odd number of elements
    temp_list = [30, 40, 20]
    result = Lab_2.calc_median_temp(temp_list)
    assert result == 30

    # Test with an even number of elements
    temp_list = [30, 40, 20, 50]
    result = Lab_2.calc_median_temp(temp_list)
    assert result == 35.0

    # Test with a single value
    temp_list = [25]
    result = Lab_2.calc_median_temp(temp_list)
    assert result == 25
