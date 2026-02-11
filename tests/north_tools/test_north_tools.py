def test_importing_north_tool():
    # this will raise an exception if pydantic model validation fails for the north tool
    from foobar.north_tools.my_north_tool import (
        north_tool_entry_point,
    )

    assert (
        north_tool_entry_point.id_url_safe == 'foobar_my_north_tool'
        or north_tool_entry_point.id == 'nomad-north-foobar'
    ), 'NORTHtool entry point has incorrect id or id_url_safe'
