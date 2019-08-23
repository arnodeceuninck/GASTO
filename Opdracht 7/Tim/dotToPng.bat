@For %%A In (*.dot
) Do dot -Tpng %%A -o %%A.png