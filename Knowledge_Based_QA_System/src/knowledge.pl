name('jahangirnagar university').
breif_description('Jahangirnagar University is a public university in Bangladesh, \c
	based in Savar Upazila, Dhaka. It is one of the top and only fully residential \c
	universities in Bangladesh. There are 34 departments, 4 institutes under six faculties.').
location('jahangirnagar university stands on the west side of the Asian Highway, \c
	popularly known as the Dhaka-Aricha Road, and is 32 kilometres away from the capital').
established('jahangirnagar university', '1970').
first_vice_chancellor('Mafizuddin Ahmed (PhD in chemistry, Penn State)').
current_vice_chancellor('Professor Doctor Farzan Islam').
history('The university was established in 1970 by the Jahangirnagar Muslim University \c
	Ordinance of the government of Pakistan. Its first vice-chancellor, Mafizuddin Ahmed \c
	(PhD in chemistry, Penn State) took up office on 24 September 1970. The first group of \c
	students, a total of 150, were enrolled in four departments: Economics, Geography, \c
	Mathematics, and Statistics. Its formal inauguration was delayed until 12 January 1971, \c
	when the university was launched by Rear Admiral S. M. Ahsan, the chancellor.').
area('697.56 acres which is 2.8 square kilometres').
number_of_faculties('6').
number_of_departments('34').
number_of_institutes('4').
faculty('faculty of mathematical and physical science').
faculty('faculty of biological science').
faculty('faculty of social science').
faculty('faculty of arts and humanities').
faculty('faculty of business studies').
faculty('faculty of law').

faculties('faculty of mathematical and physical science, \c
	faculty of biological science, \c
	faculty of social science, \c
	faculty of arts and humanities, \c
	faculty of business studies, \c
	faculty of law').

departments('department of computer science and engineering, \c
	department of mathematics, \c
	department of physics, \c
	department of environmental science, \c
	department of chemistry, \c
	department of statistics, \c
	department of geological science, \c
	department of botany, \c
	department of zoology, \c
	department of biochemistry and molecular biology, \c
	department of microbiology, \c
	department of pharmacy, \c
	department of public health and informatics, \c
	department of biotechnology and genetic engineering, \c
	department of anthropology, \c
	department of economics, \c
	department of government and politics,
	department of geography and environment, \c
	department of public administration, \c
	department of urban and regional planning, \c
	department of archaeology, \c
	department of bangla, \c
	department of drama and dramatics, \c
	department of english, \c
	department of fine arts, \c
	department of history, \c
	department of international relations, \c
	department of journalism and media studies, \c
	department of philosophy, \c
	department of accounting and information systems, \c
	department of finance and banking, \c
	department of marketing, \c
	department of management studies, \c
	department of accounting and information systems, \c
	department of finance and banking, \c
	department of marketing, \c
	department of management studies').

departments_under_faculty('faculty of mathematical and physical science','department of computer science and engineering').
departments_under_faculty('faculty of mathematical and physical science','department of mathematics').
departments_under_faculty('faculty of mathematical and physical science','department of physics').
departments_under_faculty('faculty of mathematical and physical science','department of environmental science').
departments_under_faculty('faculty of mathematical and physical science','department of chemistry').
departments_under_faculty('faculty of mathematical and physical science','department of statistics').
departments_under_faculty('faculty of mathematical and physical science','department of geological science').

departments_under_faculty('faculty of biological science','department of botany').
departments_under_faculty('faculty of biological science','department of zoology').
departments_under_faculty('faculty of biological science','department of biochemistry and molecular biology').
departments_under_faculty('faculty of biological science','department of microbiology').
departments_under_faculty('faculty of biological science','department of pharmacy').
departments_under_faculty('faculty of biological science','department of public health and informatics').
departments_under_faculty('faculty of biological science','department of biotechnology and genetic engineering').

departments_under_faculty('faculty of social science','department of anthropology').
departments_under_faculty('faculty of social science','department of economics').
departments_under_faculty('faculty of social science','department of government and politics').
departments_under_faculty('faculty of social science','department of geography and environment').
departments_under_faculty('faculty of social science','department of public administration').
departments_under_faculty('faculty of social science','department of urban and regional planning').

departments_under_faculty('faculty of arts and humanities','department of archaeology').
departments_under_faculty('faculty of arts and humanities','department of bangla').
departments_under_faculty('faculty of arts and humanities','department of drama and dramatics').
departments_under_faculty('faculty of arts and humanities','department of english').
departments_under_faculty('faculty of arts and humanities','department of fine arts').
departments_under_faculty('faculty of arts and humanities','department of history').
departments_under_faculty('faculty of arts and humanities','department of international relations').
departments_under_faculty('faculty of arts and humanities','department of journalism and media studies').
departments_under_faculty('faculty of arts and humanities','department of philosophy').

departments_under_faculty('faculty of business studies','department of accounting and information systems').
departments_under_faculty('faculty of business studies','department of finance and banking').
departments_under_faculty('faculty of business studies','department of marketing').
departments_under_faculty('faculty of business studies','department of management studies').

departments_under_faculty('faculty of law','department of law and justice').

department('department of computer science and engineering').

about_department_of_computer_science_and_engineering('the department of computer science and \c
    engineering of jahangirnagar university is one \c
    of the leading cse department in bangladesh. \c
	since its inception in 1991, the Department is playing a vital role in developing \c
	skilled ict professional and researchers. \c
	the department selects very good quality national and international students in each academic year.
	professor doctor mohammad imdadul islam the present chairman of this department').

chairman_of_cse('department of computer science and engineering', 'professor doctor mohammad imdadul islam').
developers('shamim imtiaz and kamrul hasan tusher').
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

introduction(X, Y):- name(X), breif_description(Y).
history(X, Y):- name(X), history(Y).
location(X, Y):- name(X), location(Y).
area(X, Y):- name(X), area(Y).
first_vice_chancellor(X, Y):- name(X), first_vice_chancellor(Y).
vice_chancellor(X, Y):- name(X), current_vice_chancellor(Y).
number_of_faculties(X, Y):- name(X), number_of_faculties(Y).
number_of_departments(X, Y):- name(X), number_of_departments(Y).
number_of_institutes(X, Y):- name(X), number_of_institutes(Y).

faculties(X, Y):- name(X), faculties(Y).
departments(X, Y):- name(X), departments(Y).
departments_under_faculty(X, Y, Z):- name(X), faculty(Y), departments_under_faculty(Y, Z).
about_department_of_computer_science_and_engineering(X, Y):-
	name(X), about_department_of_computer_science_and_engineering(Y).