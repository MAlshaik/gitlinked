

sample_users = [{
    "id": "user1",
    "description": "data scientist, Topological data analysis",
    "skills": "jupyter notebook, data science",
}, {
    "id": "user2",
    "description": "frontend developer",
    "skills": "javascript"
}, {
    "id": "user3",
    "description": "ml engineer",
    "skills": "jupyter notebook"
}, {
    "id": "user4",
    "description": "web and mobile app developer",
    "skills": "dart, flutter, html"
}]



sample_repositories = [{
    "id": "repository1",
    "languages": "python",
    "description": "language",
}, {
    "id": "repository2",
    "languages": "javascript",
    "description": "website",
}, {
    "id": "repository3",
    "languages": "java",
    "description": "android",
}, {
    "id": "repository4",
    "languages": "swift",
    "description": "mobile app",
}, {
    "id": "repository5",
    "languages": "python, jupyter notebook",
    "description": "#  Topological Signal Processing for Dynamical Systems\n\nThis repository contains the content for a [minitutorial](https://www.siam.org/conferences/cm/program/minitutorials/ds23-minitutorials) for the [2023 SIAM Conference on Applications of Dynamical Systems (DS23)](https://www.siam.org/conferences/cm/conference/ds23). **If you're planning to attend the minitutorial, please see [the instructions below](#accessing-the-content) for some setup that will help get us up and running faster.**\n\n- [Part I Information](https://meetings.siam.org/sess/dsp_programsess.cfm?SESSIONCODE=75586): Mon May 15, 1:20-3:20PM \n- [Part II Information](https://meetings.siam.org/sess/dsp_programsess.cfm?SESSIONCODE=77160): Mon May 15 4:45-6:45PM\n- Both sessions in Lloyd Center Ballroom - 1st Level\n\nContributors to this minitutorial are:\n\n- [Firas Khasawneh](https://firaskhasawneh.com)\n- [Elizabeth Munch](https://elizabethmunch.com)\n- [Max Chumley](https://www.maxchumley.com)\n- [Danielle Barnes](https://github.com/barnesd8) \n- [Sunia Tanweer](https://stanweer1.github.io)\n\n## Abstract\n\nPersistent homology, the flagship method of topological data analysis (TDA), can be used to provide a quantitative summary of the shape of data.  There is now extensive work using the following pipeline. Start with a realization of a dynamical system, perhaps after reconstruction from time series data. Treat this data as a discrete metric space, and construct a filtration of a simplicial complex that encodes information about the shape.  Then, use persistent homology to determine when structures appear and disappear in this filtration, which can in turn be used as input to tools such as machine learning models. \n\nThis mini-tutorial will cover the basics of each piece of the aforementioned pipeline, as well as show more recently studied modifications that show a great deal of promise for future analysis of dynamical systems with TDA. This tutorial will be run using active learning, with participants coding examples in python in provided Jupyter notebooks, making extensive use of the open-source package [teaspoon](https://github.com/TeaspoonTDA/teaspoon). \n\n![](figures/big_picture.png)\n\n## Schedule \n\n\n### Session 1: Persistent Homology Basics\n\n0. Welcome Remarks and Introduction (5 minutes)\n   - [Slides](https://github.com/TeaspoonTDA/2023-SIAM-DS-TDA-Minitutorial/blob/main/1-0-Welcome.ipynb)\n   - Presenter: Firas Khasawneh & Liz Munch\n1. Simplicial complexes & Homology (30 min)\n   - [Slides](https://github.com/TeaspoonTDA/2023-SIAM-DS-TDA-Minitutorial/blob/main/1-1-SimplicialCpx_Homology.ipynb)\n   - [Jupyter notebook](https://github.com/TeaspoonTDA/2023-SIAM-DS-TDA-Minitutorial/blob/main/1-1-Wkst-SimplicialCpx_Homology.ipynb) \n   - Presenter: Liz Munch\n2. Persistent homology (30 min)\n   - [Slides](https://github.com/TeaspoonTDA/2023-SIAM-DS-TDA-Minitutorial/blob/main/1-2-PersistentHomology.ipynb) \n   - [Jupyter notebook](https://github.com/TeaspoonTDA/2023-SIAM-DS-TDA-Minitutorial/blob/main/1-2-Wkst-PersistentHomology.ipynb) \n   - Presenter: Liz Munch\n3. Persistence Pipelines: Rips & Images (30 min)\n   - [Slides](https://github.com/TeaspoonTDA/2023-SIAM-DS-TDA-Minitutorial/blob/main/1-3-PersistencePipelines.ipynb)\n   - [Jupyter notebook](https://github.com/TeaspoonTDA/2023-SIAM-DS-TDA-Minitutorial/blob/main/1-3-PersistencePipelines.ipynb) \n   - Presenter: Firas Khasawneh \n4. Distances on persistence diagrams & Vectorization (10 min)\n   - [Slides](https://github.com/TeaspoonTDA/2023-SIAM-DS-TDA-Minitutorial/blob/main/1-4-DistancesAndVectorization.ipynb)\n   - Presenter: Danielle Barnes\n5. Session 1 Wrap up (5 minutes)\n   - Slides\n   - Presenter: Firas Khasawneh & Liz Munch\n   \n### Session 2: Using Persistence for Signal Processing\n\n0. Welcome Remarks and Introduction (5 min)\n   - [Slides](https://github.com/TeaspoonTDA/2023-SIAM-DS-TDA-Minitutorial/blob/main/2-0-Welcome.ipynb)\n   - Presenter: Firas Khasawneh & Liz Munch\n1. Embedding of Time series (40 min)\n   - [Slides](https://github.com/TeaspoonTDA/2023-SIAM-DS-TDA-Minitutorial/blob/main/2-1-Embedding.ipynb)\n   - [Jupyter notebook](https://github.com/TeaspoonTDA/2023-SIAM-DS-TDA-Minitutorial/blob/main/2-1-Wkst-Embedding.ipynb)\n   - Presenter: Max Chumley\n2. Graph representations of time series (30 min)\n   - [Slides](https://github.com/TeaspoonTDA/2023-SIAM-DS-TDA-Minitutorial/blob/main/2-2-GraphTimeSeries.ipynb)\n   - [Jupyter notebook](https://github.com/TeaspoonTDA/2023-SIAM-DS-TDA-Minitutorial/blob/main/2-2-Wkst-GraphTimeSeries.ipynb)\n   - Presenter: Max Chumley\n3. Crocker plots (20 min)\n   - [Slides](https://github.com/TeaspoonTDA/2023-SIAM-DS-TDA-Minitutorial/blob/main/2-3-CrockerPlots.ipynb) \n   - [Jupyter notebook](https://github.com/TeaspoonTDA/2023-SIAM-DS-TDA-Minitutorial/blob/main/2-3-Wkst-CrockerPlots.ipynb)\n   - Presenter: Sunia Tanweer\n4. Identifying P-bifurcations in Stochastic Systems (10 min)\n   - [Slides](https://github.com/TeaspoonTDA/2023-SIAM-DS-TDA-Minitutorial/blob/main/2-4-Stochastics.ipynb)\n   - [Jupyter notebook](https://github.com/TeaspoonTDA/2023-SIAM-DS-TDA-Minitutorial/blob/main/2-4-Wkst-Stochastics.ipynb)\n   - Presenter: Sunia Tanweer\n5. Session 2 Wrap up (5 min)\n   - [Slides](https://github.com/TeaspoonTDA/2023-SIAM-DS-TDA-Minitutorial/blob/main/2-5-Wrapup.ipynb)\n   - Presenter: Firas Khasawneh & Liz Munch\n\n## Accessing the content\n\nThis minitutorial will be run in an active learning style. We will present basic introductions to the concepts followed by time to try out examples provided in the Jupyter notebooks in this GitHub repository.  We highly recommend that you bring a laptop to the workshop. If at all possible, we also recommend following the below instructions in advance in case of issues. We will have two ways to access the content during the workshop itself:\n\n- Locally installed on your machine. You will need to clone the repository and get the code installed in advance. Unfortunately we cannot provide much in the way of install help due to the size and nature of the workshop. So, if local install doesn't work, we have provided.....\n- Remote servers where you will be able to access all the material during the workshop. Please note that these servers will only be active during the workshop itself. \n\nNote that the remote version will require a GitHub account, so we recommend making one in advance in case of issues, even if planning to run the code locally.\n\n### Local Install Instructions\n\n#### Teaspoon\n\nTo install [teaspoon](https://github.com/TeaspoonTDA/teaspoon) locally, please follow the directions provided in [Getting Started](https://teaspoontda.github.io/teaspoon/installation.html#).  There are two system dependencies:\n-  [cmake](https://cmake.org/install/) and \n-  [boost for Unix](https://www.boost.org/doc/libs/1_66_0/more/getting_started/unix-variants.html) or [boost for Windows](https://www.boost.org/doc/libs/1_62_0/more/getting_started/windows.html).  \n\nWhile we make every effort to ensure compatibility across operating systems, we cannot guarantee you will not encounter install issues.\n\nIn addition to teaspoon, `RISE` and `giotto-tda` are required for use of the slide decks and specific portions of the minitutorial.  Once system dependencies are installed, to install the required python packages you should be able to run:\n\n``` \n\npip install teaspoon\npip install RISE\npip install giotto-tda\n```\n\n#### Clone the repo\n\nYou will want to clone this repository to be of use in your local machine. We list two options below for cloning the repo.\n\n##### Clone using GiHub Desktop\nThe first option to clone the repository is via [GitHub Desktop](https://desktop.github.com/), which is available for Windows and macOS. After installing the app, go to *File>Clone Repository*, click the <kbd>URL</kbd> tab, and enter the repository's address. Choose where the local path for the repository, and hit <kbd>Clone</kbd>.  \n\n##### Clone using Git\nAssuming you already have ssh setup for GitHub (see [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) if you need additional directions) the repository can be cloned with the following command.\n\n```\ngit clone git@github.com:TeaspoonTDA/2023-SIAM-DS-TDA-Minitutorial.git\n```\n\n### Remote Connection Instructions\n\nTo connect remotely, you will need to setup a GitHub account and then at the time of the workshop, connect to a remote server. Then all code and workbooks will be run directly via web browser. \n\n#### Github account creation\n\nPlease follow the [GitHub signup instructions](https://docs.github.com/en/get-started/signing-up-for-github/signing-up-for-a-new-github-account).\n\n#### Server Login Information\n\n**Note:** These links and instructions will not be updated until the minitutorial begins.\n\nTo run your computations on a provided Jupyter Server, login by choosing one of the URL's below as instructed:\n\n- [Server 1](https://9g72.short.gy/server1)\n- [Server 2](https://9g72.short.gy/server2)\n\nYou must use the same URL to login for the full minitutorial since these are specific servers where your work will be located.  At the end of the conference, you will also need to download your work as the servers will not be available after the conference ends.\n\n# Funding \n\nWe are grateful to the following agencies for their support of this project. \n\n- The Air Force Office of Scientific Research under Award FA9550-22-1-0007.\n- The National Science Foundation under awards CCF-2106578, CCF-1907591, and CCF-2142713. \n- Michigan State University \n- The Society for Industrial and Applied Mathematics\n",
}]



sample_relationships = [[
    "user1",
    "repository1"
], [
    "user2",
    "repository2"
], [ 
    "user3",
    "repository1"
], [
    "user4",
    "repository3"
], [
    "user4",
    "repository4"
], [
    "user1", 
    "user3"
], [
    "user1",
    "user2"
]]


