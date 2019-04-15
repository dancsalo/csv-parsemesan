# Parsemesan
This grate repository will unbrielievably parse your CSV string and
return a Python dictionary with headers and rows of data. You cheddar
believe I put some gouda tests in here.

All cheesiness aside, the goal of this project is to allow the parsing
of CSV files to stand alone as a separate service and remove the
burden from the frontend code of Datasmith and later Wordsmith. This
project will most likely expand to include other data formats.

## Getting Started

##### Installation
Python 3.6+ is required. From repo root, run `pip install -r requirements.txt`

##### Tests
From repo root, run `pytest`
From repo root, run `pylint parsemesan tests`

##### Coverage

From repo root, run `coverage run -m pytest && coverage html`

## Usage

Here's an exaample:

a = [['Commentary', 'Commentary (Analyst Excesses)', 'Commentary (Manager Excesses)', 'credit_analyst', 'credit_manager', 'Dimension Selection', 'Excess Commentary', 'sector', 'Chart - 100%', 'COLOR - Limit Util by Dim', 'Exceeds Limit', 'Limit Overage', 'LOD - Limit Util by Dim', 'REF LINE - Requires Commentary', 'today_limit', 'today_utilization'], [None, None, None, 'Jan Ylvhed', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Financial Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 0, None], ['Test commentary, derp...', None, None, 'Greta Artoft', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Healthcare', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 0, None], [None, None, None, 'Jan Ylvhed', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Manufacturing & High Tech', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 0, None], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Manufacturing & High Tech', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 0, None], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Manufacturing & High Tech', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 0, None], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Manufacturing & High Tech', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 0, None], [None, None, None, 'Jan Ylvhed', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Manufacturing & High Tech', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 0, None], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Public Sector', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 0, None], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 0, None], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 0, None], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 0, None], [None, None, None, 'Jan Ylvhed', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 0, None], [None, None, None, 'Jan Ylvhed', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 0, None], [None, None, None, 'Jan Ylvhed', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 0, None], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 0, None], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Communications', 1, 'GREEN', 1, 30214.811, 0.5135656368838382, 1500000, 0, 30214.811], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Financial Services', 1, 'GREEN', 1, 2106.29, 0.5135656368838382, 1500000, 0, 2106.29], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 1, 108.15, 0.5135656368838382, 1500000, 0, 108.15], ['Test commentary, derp...', None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Healthcare', 1, 'GREEN', 1, 3075044, 0.5135656368838382, 1500000, 0, 3075044], [None, None, None, 'Jan Ylvved', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 5000000, 373428.09], [None, None, None, 'Berta Sellliden', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 93500000, 16107886], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Communications', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 1000000, 11.39], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Communications', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 3020.8196, 23.77], ['Test commentary, derp...', None, None, 'Jan Ylvhed', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Healthcare', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 10000000, 32429.289], ['Test commentary, derp...', None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Healthcare', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 6003021, 16701.711], [None, None, None, 'Jan Ylvhed', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Manufacturing & High Tech', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 1070000, 1102.29], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Manufacturing & High Tech', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 85889064, 544500.44], [None, None, None, 'Jan Ylvhed', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Communications', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 5000000, 82378.859], ['Test commentary, derp...', None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Healthcare', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 5010150, 152854.53], [None, None, None, 'Greta Artoft', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Manufacturing & High Tech', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 1907790.1, 80945.438], ['Test commentary, derp...', None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Healthcare', 1, 'GREEN', 1, 41.59668, 0.5135656368838382, 1500000, 3624.9834, 3666.5801], [None, None, None, 'Lennart Askved', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Manufacturing & High Tech', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 616724.94, 328826.09], [None, None, None, 'Justus Bernklint', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Life Sciences', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 916486.44, 916486.44], [None, None, None, 'Lennart Askved', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 2477590.5, 1044576.9], [None, None, None, 'Jan Ylvhed', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 2144906, 1462882.2], [None, None, None, 'Lennart Askved', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Manufacturing & High Tech', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 1212596.4, 1212596.4], [None, None, None, 'Justus Bernklint', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Public Sector', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 2398537.2, 2398537.2], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Manufacturing & High Tech', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 259000000, 50843092], [None, None, None, 'Greta Artoft', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 104052780, 104052770], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Manufacturing & High Tech', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 47013000, 85740.406], [None, None, None, 'Sune Myrrbråten', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Public Sector', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 45000000, 5363.8101], [None, None, None, 'Jan Ylvhed', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Financial Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 8000000, 94502.898], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Financial Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 3020.8196, 79.459999], [None, None, None, 'Greta Artoft', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Communications', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 1271860.1, 175041.05], [None, None, None, 'Jan Ylvhed', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Financial Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 272526.25, 62968.18], [None, None, None, 'Justus Bernklint', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Manufacturing & High Tech', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 5000000, 654000], [None, None, None, 'Jan Ylvhed', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 1750000, 288552.72], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 2382218.2, 495422.28], [None, None, None, 'Jan Ylvhed', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 405180.25, 87751.008], [None, None, None, 'Jan Ylvhed', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 5168704, 937216.19], [None, None, None, 'Jan Ylvved', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Manufacturing & High Tech', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 8926774, 1317570.9], [None, None, None, 'Svante Alinkleven', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Communications', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 61926800, 10118313], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 22000000, 192199.09], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 604163.88, 58.580002], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Financial Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 12772871, 384991.44], [None, None, None, 'Justus Bernklint', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Financial Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 168766.69, 168766.69], [None, None, None, 'Justus Bernklint', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 556815, 307574.38], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Communications', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 9439.7344, 9439.7305], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Communications', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 341066.12, 341066.12], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Communications', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 2077731.6, 2077731.6], [None, None, None, 'Jan Ylvved', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Energy & Utilities', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 11900778, 6240900], ['Test commentary, derp...', None, None, 'Justus Bernklint', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Healthcare', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 2682487.8, 1658618.6], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 76998.289, 76998.289], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Manufacturing & High Tech', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 90624.586, 54579.32], [None, None, None, 'Justus Bernklint', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 206019.89, 114937.45], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Manufacturing & High Tech', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 244439.02, 244439.02], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 211928.62, 211928.62], ['Test commentary, derp...', None, None, 'Jan Ylvhed', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Healthcare', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 1365562.1, 1365562.1], ['Test commentary, derp...', None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Healthcare', 1, 'GREEN', 1, 32789, 0.5135656368838382, 1500000, 2500000, 2532789], [None, None, None, 'Sune Myrrbråten', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 198800000, 85443328], [None, None, None, 'Eugen Hernfjorden', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Public Sector', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 67661056, 56763608], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Manufacturing & High Tech', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 60000000, 7357429.5], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Financial Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 337325.84, 337325.84], [None, None, None, 'Justus Bernklint', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Manufacturing & High Tech', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 55482.137, 55482.141], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Manufacturing & High Tech', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 47246.191, 47246.191], [None, None, None, 'Jan Ylvhed', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Communications', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 436480, 392334.62], [None, None, None, 'Jan Ylvhed', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Financial Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 694184.31, 597519.44], ['Test commentary, derp...', None, None, 'Jan Ylvhed', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Healthcare', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 220000, 215000], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Manufacturing & High Tech', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 47246.191, 47246.191], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 105108.77, 105108.77], [None, None, None, 'Justus Bernklint', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Manufacturing & High Tech', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 2288468.5, 2288468.5], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 1, 84081.5, 0.5135656368838382, 1500000, 6752256.5, 6836338], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 2624052.8, 2624052.8], [None, None, None, 'Lennart Askved', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Financial Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 2078323.8, 1454082], [None, None, None, 'Justus Bernklint', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Financial Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 6046498, 6046498], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Manufacturing & High Tech', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 1233125.5, 1233125.5], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 3228007, 3159031.8], [None, None, None, 'Lennart Askved', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Life Sciences', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 20069946, 20069946], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 295000000, 218812800], ['Test commentary, derp...', None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Healthcare', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 115492880, 107895490], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 175841410, 175841410], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Communications', 1, 'GREEN', 1, 5964.5156, 0.5135656368838382, 1500000, 153000, 158964.52], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Communications', 1, 'GREEN', 1, 1147.4688, 0.5135656368838382, 1500000, 365519.16, 366666.62], [None, None, None, 'Paula Tilstål', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 617208.5, 617208.5], [None, None, None, 'Jan Ylvhed', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Manufacturing & High Tech', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 2086276.9, 971318.38], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Energy & Utilities', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 573709.81, 573709.81], [None, None, None, 'Justus Bernklint', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Financial Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 231189.78, 203736.67], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Financial Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 34888.152, 34888.148], ['Test commentary, derp...', None, None, 'Jan Ylvhed', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Healthcare', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 587120.19, 549999.75], [None, None, None, 'Justus Bernklint', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Manufacturing & High Tech', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 31255.174, 31255.17], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 433839.31, 433839.31], [None, None, None, 'Lennart Askved', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 9384.1641, 9378.6602], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 172384.08, 172384.06], ['Test commentary, derp...', None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Healthcare', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 2348093, 2348093], [None, None, None, 'Jan Ylvhed', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Manufacturing & High Tech', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 3666585.2, 3666585.2], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 1760235.1, 1760235.1], ['Test commentary, derp...', None, None, 'Set Mildånger', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Healthcare', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 10428130, 8867574], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 2768279, 2698438], [None, None, None, 'Paula Tilstål', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 21388414, 21388414], [None, None, None, 'Sune Myrrbråten', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Retail & Services', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 208040000, 90590552], [None, None, None, 'Paul Munz', 'Linda Venfjärd', 'Linda Venfjärd', None, 'Energy & Utilities', 1, 'GREEN', 0, 0, 0.5135656368838382, 1500000, 10963175, 10708545]]
h = parse_data('arrays', a)
print(h['result'])

## Documentation

### API

**`parse_data`**

##### Params

 - **{str}**: `source_type` the type of data source (`arrays`, `csv`, `unicode`)
 - **{*}**: `input_data` CSV `{bytes}` or Python `{list}` or Python `{str}` (which is Unicode)

##### Return

 - **{dict}**: Python object with following spec:
     ```
    {
        "errors": [
            <dict>
        ]
        "result": {
            "headers": <list of {str}>
            "rows": <list of lists of {str}>
        }
    }
    ```

**`get_valid_formats`**

##### Params

 - No inputs required.

##### Return

 - **{dict}**: Python object with following spec:
     ```
    {
        "formats": <list of {str}>
    }
    ```


### Types and Errors

 - `byte_string`: a raw Python `bytes` array. Does not apply to `source_type='arrays'`. `EncodingError` raised if not valid.
 - `stream`: a Python object that reads the data sequentially. `FileTypeError` raised if not valid.
 - `data`: a Python dictionary with keys `headers` and `rows` (see below). `DataError` raised if not valid.

### Pipelines
Each pipeline combines a `parser` and at least one `validator`, as shown in the `pipelines/` directory.

#### Arrays
The `input_data` is a Python `{list}` of `{lists}` containing the rows of data.

1. Parse or reorganize the object into `data`.
2. Validate the `data`'s rows and headers as proper tabular.

`data` is returned as described above.

#### CSV
The `input_data` is a Python `{bytes}` object containing an encoded CSV table.

1. Detect `input_data` encoding using the `chardet` module.
2. Validate the `byte_string`'s encoding by calling the native `.decode(encoding)` function.
3. Convert it to a `stream` with the native `ioString` module.
4. Validate the `stream`'s file type by eliminating other common possibilities of files (`.html`, `.xml`).
5. Parse the stream into `data` using the native `csv` module.
6. Validate the `data`'s rows and headers as proper tabular.

`data` is returned as described above.

#### Unicode
The `input_data` is a Python `{str}` object (which is Unicode in Python 3) containing an encoded CSV table.

1. Convert the string to a `stream` with the native `ioString` module.
2. Validate the `stream`'s file type by eliminating other common possibilities of files (`.html`, `.xml`).
3. Parse the stream into `data` using the native `csv` module.
4. Validate the `data`'s rows and headers as proper tabular.

`data` is returned as described above.

