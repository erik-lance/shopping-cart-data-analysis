# Shopping-Cart-Data-Analysis
Read this section before committing and pushing to the repository.

# Pre-requisites
Since Python Notebooks save outputs, it is important to clear all outputs before committing and pushing to GitHub. This can be done by selecting `Cell` > `All Output` > `Clear` from the menu bar.

There is also an automated way to do this. In the terminal, run the following command:

```shell
pip install nbstripout
nbstripout --install

git config filter.nbstripout.clean 'nbstripout'
git config filter.nbstripout.smudge cat
git config filter.nbstripout.required true
```
This will install the nbstripout package and configure Git to automatically strip out the outputs of all notebooks before committing them. This will make the diffs of the notebooks much easier to read and review.