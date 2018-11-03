import dicttoxml
from xml.dom.minidom import parseString

d1 = [ {"about": "Merge pull request", "author": "EricJFisher", "datetime": "2016-12-09T20:49:33Z", "url": "https://github.com/codeschool-projects/HelloCodeSchoolProject/commit/c1174ac7d251ff47c90ae1790671931a1ccd0e4e"},
{"about": "Corrected Project URL in Readme.md", "author": "EricJFisher", "datetime": "2016-12-09T20:43:01Z", "url": "https://github.com/codeschool-projects/HelloCodeSchoolProject/commit/85aacdf63da45f29058e16cce9df5ed22a4e10cf"},
{"about": "Merge pull request", "author": "adamfortuna", "datetime": "2016-12-08T20:28:29Z", "url": "https://github.com/codeschool-projects/HelloCodeSchoolProject/commit/a4b0f0a0b9aab0c6f52dbe3f3f7c6ccb047d5202"},
{"about": "Change assertion message for task 1", "author": "eibt", "datetime": "2016-12-08T16:19:46Z", "url": "https://github.com/codeschool-projects/HelloCodeSchoolProject/commit/7b7f648ce798fcc33a3346d1a2c0f19472a03cb6"},
{"about": "Update README.md", "author": "adamfortuna", "datetime": "2016-12-08T14:40:13Z", "url": "https://github.com/codeschool-projects/HelloCodeSchoolProject/commit/3ab48d7b1ea110e0d8158109989dadedc335d121"},
{"about": "Update README.md", "author": "adamfortuna", "datetime": "2016-12-08T14:36:51Z", "url": "https://github.com/codeschool-projects/HelloCodeSchoolProject/commit/b6e3af9955786543d2fab07ae415d8085cdbb31e"},
{"about": "Update LICENSE.txt", "author": "adamfortuna", "datetime": "2016-11-02T16:30:33Z", "url": "https://github.com/codeschool-projects/HelloCodeSchoolProject/commit/ff77f689b8e3cc994696e9d5e0ba32b582bc2d08"},
{"about": "Create LICENSE.txt", "author": "adamfortuna", "datetime": "2016-11-02T16:28:53Z", "url": "https://github.com/codeschool-projects/HelloCodeSchoolProject/commit/84d1515f84d7ae92e0b164b2822321591b03d9ed"},
{"about": "Updated task 1 to reflect state of the HTML", "author": "adamfortuna", "datetime": "2016-10-24T15:06:54Z", "url": "https://github.com/codeschool-projects/HelloCodeSchoolProject/commit/8ac62660b2d98c7ab5ea90cc36b151441149881a"},
{"about": "Added screenshot with finished example", "author": "adamfortuna", "datetime": "2016-10-24T15:06:43Z", "url": "https://github.com/codeschool-projects/HelloCodeSchoolProject/commit/4f517f568d9e44a962af83c4da5c45bf3c49905f"},
{"about": "Updated tests to include tagging and add error messages", "author": "adamfortuna", "datetime": "2016-08-30T11:55:30Z", "url": "https://github.com/codeschool-projects/HelloCodeSchoolProject/commit/8cd39c6e172383f187c0a5fbd664e08882f88139"},
{"about": "Initial commit", "author": "drewbarontini", "datetime": "2016-08-15T12:44:16Z", "url": "https://github.com/codeschool-projects/HelloCodeSchoolProject/commit/ab1f82a44130db040438c36f10135fa130b85ba8"},
{"about": "Corrected Demo location and bad link", "author": "EricJFisher", "datetime": "2016-12-09T21:04:29Z", "url": "https://github.com/codeschool-projects/HelloCodeSchoolProject/commit/bd34099cd06fd1de7ca6ece607781d5d8ba1257e"},
{"about": "Merge pull request", "author": "EricJFisher", "datetime": "2016-12-09T20:49:47Z", "url": "https://github.com/codeschool-projects/HelloCodeSchoolProject/commit/7e726e36c2321696378c205389f52a768c5c1637"},
{"about": "Corrected project Url in Readme.md and branch name", "author": "EricJFisher", "datetime": "2016-12-09T20:44:55Z", "url": "https://github.com/codeschool-projects/HelloCodeSchoolProject/commit/55f99331dff2ac0d0cd5f30a7ddbc63bf7883e3d"},
{"about": "Added example answer", "author": "adamfortuna", "datetime": "2016-10-24T15:07:31Z", "url": "https://github.com/codeschool-projects/HelloCodeSchoolProject/commit/cb8f3b19843e32e2b0549cf7308c68f567993692"},
{"about": "Updated task 1 to reflect state of the HTML", "author": "adamfortuna", "datetime": "2016-10-24T15:06:54Z", "url": "https://github.com/codeschool-projects/HelloCodeSchoolProject/commit/8ac62660b2d98c7ab5ea90cc36b151441149881a"},
{"about": "Added screenshot with finished example", "author": "adamfortuna", "datetime": "2016-10-24T15:06:43Z", "url": "https://github.com/codeschool-projects/HelloCodeSchoolProject/commit/4f517f568d9e44a962af83c4da5c45bf3c49905f"},
{"about": "Updated tests to include tagging and add error messages", "author": "adamfortuna", "datetime": "2016-08-30T11:55:30Z", "url": "https://github.com/codeschool-projects/HelloCodeSchoolProject/commit/8cd39c6e172383f187c0a5fbd664e08882f88139"},
{"about": "Initial commit", "author": "drewbarontini", "datetime": "2016-08-15T12:44:16Z", "url": "https://github.com/codeschool-projects/HelloCodeSchoolProject/commit/ab1f82a44130db040438c36f10135fa130b85ba8"} ]

d2 = [ {"dictionary": {"test/index_test.js": "assert equal window $ title length 1 Make sure to create a `title` element. it should have a title   @title function it should have a title   @title function assert notEqual window $ title text Make sure to set the content of the `title` element to your Code School username. ", "count": 1}},
{"dictionary": {"README.md": "Setup Git [ How to Setup Git for Code School Projects in 5 Minutes ](#) Git ", "count": 1}},
{"dictionary": {"LICENSE.txt": "", "count": 1}},
{"dictionary": {"README.md": "Getting Started Hello Code School codeschool Hello Code School code-school Prerequisites Checking Your Work Hello Code School codeschool Hello Code School code-school Running Tests Locally ", "count": 1}},
{"dictionary": {"LICENSE.txt": "", "count": 1}},
{"dictionary": {"README.md": "Getting Started Hello Code School codeschool Hello Code School code-school Prerequisites Checking Your Work Hello Code School codeschool Hello Code School code-school Running Tests Locally ", "count": 1}},
{"dictionary": {"README.md": "`http://<username>.github.io/HelloCodeSchoolProject/` `answer` http://codeschool.github.io/HelloCodeSchoolProject/ Another Answer `solution` ", "count": 1}},
{"dictionary": {"test/index_test.js": "assert equal window $ title length 1 Make sure to create a `title` element. it should have a title   @title function it should have a title   @title function assert notEqual window $ title text Make sure to set the content of the `title` element to your Code School username. ", "count": 1}},
{"dictionary": {"screenshot.png": "", "count": 1}},
{"dictionary": {"README.md": "Add a Page Title Change the `title` to Create a `title` element with Add a Header Element ", "count": 1}},
{"dictionary": {"index.html": "meta charset utf-8 meta http-equiv X-UA-Compatible content IE=edge meta name viewport content width=device-width, initial-scale=1 title title head body h1 h1 ul li li li li li li ul body html ", "count": 1}},
{"dictionary": {"README.md": "Getting Started Hello Code School codeschool Hello Code School code-school Prerequisites Checking Your Work Hello Code School codeschool Hello Code School code-school Running Tests Locally `http://<username>.github.io/HelloCodeSchoolProject/` ` ` http://codeschool.github.io/HelloCodeSchoolProject/ ` ` http://codeschool.github.io/HelloCodeSchoolProject/ ", "count": 1}},
{"dictionary": {"index.html": "meta charset utf-8 meta http-equiv X-UA-Compatible content IE=edge meta name viewport content width=device-width, initial-scale=1 title title head body ", "test/index_test.js": "it should have a  title function assert notEqual window $ title text (),  it should have a  title function assert equal window $ title length ,  1 ,  it should have a  function assert notEqual window $ length ,  0 it should have a  function assert notEqual window $ text (),  ,  it should have a  function assert notEqual window $ length 0 it should have a  function assert isAtLeast window $ length 1 ,  it should have at least 2 li elements function assert isAtLeast window $ li length 2 it should have content in the h1 element @h1 function assert equal window $ h1 text Hello, Code School! Make sure to set the content of your `h1` element to 'Hello, Code School!'. it should have a ul @ul function assert isAtLeast window $ ul length 1 Make sure to create a `ul` element. it should have at least 2 li elements @li function assert isAtLeast window $ li length 2 Make sure to create at least 2 `li` elements. it should have content for all `li` elements. @li function var = Make sure to include something you want to learn for each `li` element. assert notEqual window $ li:first text assert notEqual window $ li:last text ", "count": 2}},
{"dictionary": {"README.md": "Getting Started Hello Code School codeschool Hello Code School code-school Prerequisites Checking Your Work Hello Code School codeschool Hello Code School code-school Running Tests Locally `http://<username>.github.io/HelloCodeSchoolProject/` ` ` http://codeschool.github.io/HelloCodeSchoolProject/ ` ` http://codeschool.github.io/HelloCodeSchoolProject/ ", "count": 1}},
{"dictionary": {".gitignore": "", ".travis.yml": "language node_js node_js 6.2.1 notifications email false cache directories node_modules ", "README.md": "Hello Code School Getting Started Hello Code School Prerequisites Front-End Foundations * * `title` `h1` `ul` `li` Setup Git How to Setup Git for Code School Projects in 5 Minutes Build `index.html` Add a Page Title `title` Add a Header Element `h1` Create an Unordered List `ul` `li` What Do You Want to Learn? `li` Checking Your Work Hello Code School Running Tests Locally node.js $ npm install $ npm test HelloCodeSchoolProject (answer) $ npm test > hello-codeschool-project@1.0.0 test /Users/adam/code/projects/HelloCodeSchoolProject > mocha test/   Your HTML Page     \u2713 should have a different title     \u2713 should have a different h1     \u2713 should have a ul     \u2713 should have at least 2 li elements   4 passing (306ms) Making it Public `gh-pages` $ git push origin master:gh-pages `index.html` `http://<username>.github.io/HelloCodeSchoolProject/` `answer` http://codeschool.github.io/HelloCodeSchoolProject/ ", "index.html": "html lang en head meta charset utf-8 meta http-equiv X-UA-Compatible content IE=edge meta name viewport content width=device-width, initial-scale=1 title title head body body html ", "package.json": "name hello-codeschool-project version 1.0.0 description Sample Code School Project main index.js scripts test ./node_modules/.bin/mocha test/ author license ISC devDependencies chai ^3.5.0 jsdom ^9.2.1 mocha ^2.5.3 ", "test/index_test.js": "var = require jsdom = require fs = require chai assert = fs readFileSync index.html toString describe Your HTML Page function var window before function next jsdom env http://code.jquery.com/jquery.js function err w if next window = next it should have a different title function assert notEqual window $ title text Hello Code School it should have a different h1 function assert notEqual window $ h1 length 0 it should have a ul function assert notEqual window $ ul length 0 it should have at least 2 li elements function assert isAtLeast window $ li length 2 ", "count": 6}},
{"dictionary": {"README.md": "Setup Git [ How to Setup Git for Code School Projects in 5 Minutes ](#) Git `http://<username>.github.io/HelloCodeSchoolProject/` `solution` ://codeschool.github.io/HelloCodeSchoolProject/ http `solution` ://codeschool .github.io/HelloCodeSchoolProject/ https -project-demos ", "count": 1}},
{"dictionary": {"screenshot.png": "", "count": 1}},
{"dictionary": {"index.html": "meta charset utf-8 meta http-equiv X-UA-Compatible content IE=edge meta name viewport content width=device-width, initial-scale=1 title title head body ", "test/index_test.js": "it should have a  title function assert notEqual window $ title text (),  it should have a  title function assert equal window $ title length ,  1 ,  it should have a  function assert notEqual window $ length ,  0 it should have a  function assert notEqual window $ text (),  ,  it should have a  function assert notEqual window $ length 0 it should have a  function assert isAtLeast window $ length 1 ,  it should have at least 2 li elements function assert isAtLeast window $ li length 2 it should have content in the h1 element @h1 function assert equal window $ h1 text Hello, Code School! Make sure to set the content of your `h1` element to 'Hello, Code School!'. it should have a ul @ul function assert isAtLeast window $ ul length 1 Make sure to create a `ul` element. it should have at least 2 li elements @li function assert isAtLeast window $ li length 2 Make sure to create at least 2 `li` elements. it should have content for all `li` elements. @li function var = Make sure to include something you want to learn for each `li` element. assert notEqual window $ li:first text assert notEqual window $ li:last text ", "count": 2}},
{"dictionary": {"README.md": "Add a Page Title Change the `title` to Create a `title` element with Add a Header Element ", "count": 1}},
{"dictionary": {".gitignore": "", ".travis.yml": "language node_js node_js 6.2.1 notifications email false cache directories node_modules ", "README.md": "Hello Code School Getting Started Hello Code School Prerequisites Front-End Foundations * * `title` `h1` `ul` `li` Setup Git How to Setup Git for Code School Projects in 5 Minutes Build `index.html` Add a Page Title `title` Add a Header Element `h1` Create an Unordered List `ul` `li` What Do You Want to Learn? `li` Checking Your Work Hello Code School Running Tests Locally node.js $ npm install $ npm test HelloCodeSchoolProject (answer) $ npm test > hello-codeschool-project@1.0.0 test /Users/adam/code/projects/HelloCodeSchoolProject > mocha test/   Your HTML Page     \u2713 should have a different title     \u2713 should have a different h1     \u2713 should have a ul     \u2713 should have at least 2 li elements   4 passing (306ms) Making it Public `gh-pages` $ git push origin master:gh-pages `index.html` `http://<username>.github.io/HelloCodeSchoolProject/` `answer` http://codeschool.github.io/HelloCodeSchoolProject/ ", "index.html": "html lang en head meta charset utf-8 meta http-equiv X-UA-Compatible content IE=edge meta name viewport content width=device-width, initial-scale=1 title title head body body html ", "package.json": "name hello-codeschool-project version 1.0.0 description Sample Code School Project main index.js scripts test ./node_modules/.bin/mocha test/ author license ISC devDependencies chai ^3.5.0 jsdom ^9.2.1 mocha ^2.5.3 ", "test/index_test.js": "var = require jsdom = require fs = require chai assert = fs readFileSync index.html toString describe Your HTML Page function var window before function next jsdom env http://code.jquery.com/jquery.js function err w if next window = next it should have a different title function assert notEqual window $ title text Hello Code School it should have a different h1 function assert notEqual window $ h1 length 0 it should have a ul function assert notEqual window $ ul length 0 it should have at least 2 li elements function assert isAtLeast window $ li length 2 ", "count": 6}}]

d = []

for (x, y) in zip(d1, d2):
	tmp = {**x, **y}
	d.append(tmp)

xml = dicttoxml.dicttoxml(d)

dom = parseString(xml)

print(dom.toprettyxml())