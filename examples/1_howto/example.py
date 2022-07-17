# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: 'Python 3.8.10 (''env'': venv)'
#     language: python
#     name: python3
# ---

# ## How to FooBar

# +
import mypackage

if __name__ == "testing":
    from mock_data import gen_data
else:
    from example_data import gen_data
# -

gen_data()
mypackage.foo()
