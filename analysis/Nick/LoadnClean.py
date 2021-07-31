{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "4b951051",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib as plt\n",
    "import numpy as np\n",
    "    \n",
    "def LoadnClean(path):\n",
    "    \n",
    "    df1 = ( \n",
    "                pd.read_csv(path,index_col = 0)\n",
    "          )\n",
    "    df2 = ( df1\n",
    "                .drop(index=df1.index[0])\n",
    "                .rename(columns={\"X1\":\"Credit Limit\",\n",
    "                            \"X2\":\"Sex\",\n",
    "                            \"X3\":\"Education\",\n",
    "                            \"X4\":\"Marital Status\",\n",
    "                            \"X5\":\"Age\",\n",
    "                            \"X6\":\"Pay/Sept07\",\n",
    "                            \"X6\":\"PayStat/Sept05\",\n",
    "                            \"X7\":\"PayStat/Aug05\",\n",
    "                            \"X8\":\"PayStat/Jul05\",\n",
    "                            \"X9\":\"PayStat/Jun05\",\n",
    "                            \"X10\":\"PayStat/May05\",\n",
    "                            \"X11\":\"PayStat/Apr05\",\n",
    "                            \"X12\":\"Outstanding/Sept05\",\n",
    "                            \"X13\":\"Outstanding/Aug05\",\n",
    "                            \"X14\":\"Outstanding/Jul05\",\n",
    "                            \"X15\":\"Outstanding/Jun05\",\n",
    "                            \"X16\":\"Outstanding/May05\",\n",
    "                            \"X17\":\"Outstanding/Apr05\",\n",
    "                            \"X18\":\"Paid/Sept05\",\n",
    "                            \"X19\":\"Paid/Aug05\",\n",
    "                            \"X20\":\"Paid/Jul05\",\n",
    "                            \"X21\":\"Paid/Jun05\",\n",
    "                            \"X22\":\"Paid/May05\",\n",
    "                            \"X23\":\"Paid/Apr05\",\n",
    "                            \"Y\":\"Default\"\n",
    "                           })\n",
    "               .apply(pd.to_numeric)\n",
    "               .replace({'Sex': {1: \"M\", 2: 'F'}})\n",
    "               .replace({'Education': {1: \"MSc or PHd\", 2: 'BSc', 3: 'High School Diploma', 4:\"Other\"}})\n",
    "               .replace({'Marital Status': {1: \"Married\", 2: 'Single', 3: 'Other'}})\n",
    "               .replace({'Default': {1: \"True\", 0: 'False'}})\n",
    "          )\n",
    "    df2\n",
    "    df3 = ( df2\n",
    "                .assign(Payment_Score=(df2[\"PayStat/Sept05\"]+df2['PayStat/Aug05']+df2['PayStat/Jul05']+df2['PayStat/Jun05']+df2['PayStat/May05']+df2['PayStat/Apr05']+6)/6)\n",
    "                .assign(Avg_Outstanding=(df2[\"Outstanding/Sept05\"]+df2['Outstanding/Aug05']+df2['Outstanding/Jul05']+df2['Outstanding/Jun05']+df2['Outstanding/May05']+df2['Outstanding/Apr05'])/6)\n",
    "                .assign(Avg_Paid=(df2[\"Paid/Sept05\"]+df2['Paid/Aug05']+df2['Paid/Jul05']+df2['Paid/Jun05']+df2['Paid/May05']+df2['Paid/Apr05'])/6)\n",
    "                .drop([\"PayStat/Jun05\",\"PayStat/Sept05\",\"PayStat/Aug05\",\"PayStat/Jul05\",\"PayStat/May05\",\"PayStat/Apr05\"], axis=1)\n",
    "                .drop([\"Outstanding/Sept05\",\"Outstanding/Aug05\",\"Outstanding/Apr05\",\"Outstanding/Jul05\",\"Outstanding/Jun05\",\"Outstanding/May05\"], axis=1)\n",
    "                .drop([\"Paid/Sept05\",\"Paid/Aug05\",\"Paid/Apr05\",\"Paid/Jul05\",\"Paid/Jun05\",\"Paid/May05\"], axis=1)\n",
    "                .reindex(columns=[\"Credit Limit\", \"Sex\", \"Education\",\"Marital Status\",\"Age\",\"Payment_Score\",\"Avg_Outstanding\",\"Avg_Paid\",\"Default\"])\n",
    "                [df2[\"Default\"]==\"True\"]\n",
    "          )\n",
    "    df3\n",
    "    \n",
    "    return df3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "25e30c97",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5e5ddffb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "acecdf25",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
