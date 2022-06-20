import os
from util import get_names_from_csv

# Note: names are written in a way such they can be passed as a route into English or German wikipedia

# Assembled primary from https://commons.wikimedia.org/wiki/Category:Female_guards_in_Nazi_concentration_camps
# and female camp attendants in:
# https://commons.wikimedia.org/wiki/Category:Mug_shots_of_Holocaust_perpetrators,
# https://commons.wikimedia.org/wiki/Category:Belsen_trial_mugshots

female_guards = ['Alice Orlowski', 'Anna Hempel', 'Anneliese Kohlmann', 'Elisabeth Becker', 'Elisabeth Volkenrath', 'Ewa Paradies', 'Frieda Walter', 'Gerda Steinhoff', 'Gertrude Feist', 'Gertrude Saurer', 'Helene Kopper', 'Hermine Braunsteiner', 'Herta Bothe',
                 'Herta Oberheuser', 'Hertha Ehlert', 'Hilde Liesewitz', 'Hildegard Kanbach', 'Hildegard Lohbauer', 'Hildegard Neumann', 'Ilse Forste', 'Ilse Lothe', 'Irene Haschke', 'Irma Grese', 'Jenny-Wanda Barkmann', 'Juana Bormann', 'Maria Mandl', 'Therese Brandl', 'Wanda Klaff']

# Assembled from https://commons.wikimedia.org/wiki/Category:Mug_shots_of_Nazis

mugshots_of_nazis = ['August Heinrichsbauer', 'Albert Hartl', 'Arthur Nasse', 'Bernd von Brauchitsch', 'Bernhard Dietsche', 'Bernhard Schwarz', 'Bruno Grothe', 'Christoph Graf zu Stolberg-Stolberg', 'Erich Müller', 'Edwin Jung', 'Walter Letsch', 'Edward John Kerling', 'Emil Puhl', 'Erich Sparman', 'Erich Albrecht', 'Erich Darre', 'Erich Hahnenbruch', 'Erich Schroeder', 'Ernest Peter Burger', 'Ernst Buergin', 'Ernst John von Freyend', 'Ernst Korn', 'Ernst Lautz', 'Ernst Schaefer', 'Ernst Tesseraux', 'Erwin Brandt', 'Erwin von Lahousen', 'Fritz Schmelter', 'Franz Hupperschwiller', 'Franz Lenner', 'Franz Schlegelberger', 'Franz Xaver Schwarz', 'Frederich Kritzinger', 'Frederick Duquesne', 'Friedhelm Draeger', 'Friedrich Flick', 'Friedrich Jaehne', 'Friedrich Jeckeln', 'Fritz Bartels', 'Fritz Fischer', 'Fritz Gajewski', 'Fritz Grau', 'Fritz Meurer', 'Fritz Popp', 'Fritz Schwalm', 'George John Dasch', 'Gerhard Rose', 'Gregor Ebner', 'Guenther Tesch', 'Gustav Overbeck', 'Gustav von Halem', 'Günther Joel', 'Günther Nebelung', 'Heinz Scheurlen', 'Heinz Schmid-Loßberg', 'Hans Bavendamm', 'Hans Dieter Ellenbeck', 'Hans Hahl', 'Hans Johann Beck', 'Hans Kugler', 'Hans Mueller', 'Hans Petersen', 'Hans Werner Aufseß', 'Hans Zimmermann', 'Hans w Rinn', 'Harald Kuehnen', 'Heinrich Buscher', 'Heinrich Ebersberg', 'Heinrich Emmendorfer', 'Heinrich Gattineau', 'Heinrich Heinck', 'Heinrich Lohl', 'Heinrich Sellmer', 'Heinz Kaufmann', 'Helge Auleb', 'Helmut Johannsen', 'Helmuth Felmy', 'Herbert Hans Haupt', 'Herbert Huebner', 'Herbert Klemm', 'Herman Lang',
                     'Herman Otto Neubauer', 'Hermann Boehm', 'Hermann Cuhorst', 'Hermann Hartmann', 'Hermann Karoll', 'Hilar Giebel', 'Hor Wagner', 'Inge Viermetz', 'Jürgen von Klenck', 'Johannes Goebel', 'Joachim Entzian', 'Johann Gietler', 'Johannes Hermann Mueller', 'Josef Altmeyer', 'Max Jüttner', 'Karl-Heinz Bendt', 'Karl Lange', 'Karl Reinhardt (Politiker)', 'Karl Rühmer', 'Karl Leon Du Moulin-Eckart', 'Karl Donitz', 'Karl Hollidt', 'Karl Mummenthey', 'Karl Rasche', 'Karl Schroeder', 'Konrad Kaletsch', 'Konrad Meyer-Hetling', 'Konrad Radunski', 'Kurt Engert', 'Kurt Mayer', 'Kurt Schmidt-Klevenov', 'L Grauert', 'Leo Hepp', 'Leo Petri', 'Lippe Ernst Erbprinz zur', 'Lothar Fendler', 'Max Ilgner', 'Max Sollmann', 'Erwin Metzner', 'Michel Elmar', 'Paul Ohler', 'Oskar Welzl', 'Oskar Mueller', 'Oskars Dankers', 'Oswald Pohl', 'Oswald Rothaug', 'Otto Abs', 'Otto Schwarzenberger', 'Otto Ulm', 'Paul Zimmermann (SS-Mitglied)', 'Paul Bante', 'Paul Fehse', 'Paul Haefliger', 'Paul Pleiger', 'Paul Riege', 'Paul Scholz', 'Paulmann Werner', 'Philipp Heinrich Hoerlein', 'Reinhard Gehlen', 'Richard Hildebrandt', 'Richard Quirin', 'Rudolf Creutz', 'Rudolf Kerner', 'Rudolf Oeschey', 'Gustav Wilhelm Schübbe', 'Heinrich Schulz (assassin)', 'Stahl Friedrich', 'Uebelhack Friedrich', 'Ulrich Haberland', 'WP George John Dasch', 'Walter Laermann', 'Walter Staudinger', 'Kurt von Tippelskirch', 'Wolfgang Wirth', 'Werner von Hoven', 'Walter Duerrfeld', 'Walter Greiling', 'Walter Koehler', 'Walter Schellenberg', 'Walter Warlimont Detention Report', 'Werner Thiel', 'Wezel Emil', 'Wilhelm Bonatz', 'Wilhelm Rudolf Mann', 'Wilhelm von Ammon', 'Wilhelm von Ritter', 'Wilhem Keitel', 'Wilmar Hager', 'Wolfgang Mettgenberg']

# Assembled from https://commons.wikimedia.org/wiki/Category:Mug_shots_of_Holocaust_perpetrators

holocaust_perpetrators = ['Adam Ankenbrand', 'Adolf Ott', 'Adolf Pokorny', 'Adolf Theuer', 'Albert Fredrich Schwartz', 'Albert Kesselring', 'Albin Gretsch', 'Alfred Andreas Hofmann', 'Alfried Krupp von Bohlen und Halbach', 'Alice Orlowski', 'Ansgar Pichen', 'Anton Bergmeier', 'Arthur Andrae', 'Arthur Dietzsch', 'August Heinrich Bender', 'Werner Braune', 'Christof Knoll', 'Claus Schilling', 'Cornelius Schwanner', 'Edmund Veesenmayer', 'Eduard Lorenz', 'Eduard Strauch', 'Edwin Katzenellenbogen', 'Emil Buehring', 'Emil Haussmann', 'Emil Mahl', 'Emil Paul Pleissner', 'Erhard Brauny', 'Erich Dinges', 'Erich Muhsfeldt', 'Erich Zoddel', 'Ernst Biberstein', 'Ernst Girzick', 'Ernst Heinrich von Weizsäcker', 'Erwin Schulz', 'Erwin von Helmersen', 'Eugen Steimle', 'Fritz Schmelter', 'Felix Ruehl', 'Feodor Fedorenko', 'Franz Hoessler', 'Franz Kraus', 'Franz Six', 'Franz Stofel', 'Franz Xaver Trenkle', 'Franz Zinecker', 'Fridolin Puhr', 'Frieda Walter', 'Friedrich Ruppert', 'Friedrich Wetzel', 'Friedrich Karl Wilhelm', 'Fritz Becher', 'Fritz Buntrock', 'Fritz Fischer', 'Fritz Hintermayer', 'Fritz Klein', 'Fritz ter Meer', 'Günther Pancke', 'Georg Schallermair', 'Georg König', 'Georg Rickhey', 'Georg Schnitzler', 'Georg Weltz', 'Gerhard Rose', 'Gertrude Feist', 'Gertrude Sauer', 'Guido Reimer', 'Gustav Heigel', 'Gustav Nosske', 'Günther Altenburg', 'Hans-Theodor Schmidt', 'Hans Eisele', 'Hans Lammers', 'Hans Hoffmann', 'Hans Kurt Eisele', 'Hans Merbach', 'Hans Möser', 'Hans Wolf', 'Hans Wolfgang Romberg', 'Heinrich Buetefisch', 'Heinrich Buuck', 'Heinrich Oster', 'Heinrich Schmidt', 'Heinz Detmers', 'Heinz Jost', 'Heinz Schubert', 'Helene Kopper', 'Helmut Poppendick', 'Helmut Roscher', 'Herbert Kappler', 'Herman Hackman', 'Herman Helbig', 'Hermann Becker Freyseng', 'Hermann Eberle', 'Hermann Grossmann', 'Hermann Krumey', 'Hermann Pister', 'Hermann Schmitz', 'Hilde Liesewitz', 'Hubert Krautwurst',
                          'Ignatz Schlomovicz', 'Joachim Mrugoswsky', 'Joachim Ribbentrop', 'Johana Borman', 'Johann Eichelsdoerfer', 'Johann Kick', 'Johann Kirsch', 'Johann Paul Kremer', 'Josef Fuchsloch', 'Josef Hirtreiter', 'Josef Kestel', 'Josef Kilian', 'Josef Leipold', 'Josef Remmele', 'Juana Bormann', 'Justus Beyer', 'Jürgen Stroop', 'Karl Genzken', 'Karl Ernst Möckel', 'Karl Frenzel', 'Karl Krauch', 'Karl von Roques', 'Konrad Schaefer', 'Josef Kramer', 'Kurt Blom', 'Kurt Heinrich', 'Leonhard Eichberger', 'Luise Danz 1947', 'Maria Mandel Krakow', 'Martin Gottfried Weiss', 'Martin Hellinger', 'Martin Sandberger', 'Martin Sandberger', 'Mathias Graf', 'Max Johann Marcus Schobert', 'Max Pauly', 'Michael Redwitz', 'Oskar Schmitz', 'Oskar Groning', 'Oskar Helbig', 'Oskar Schroeder', 'Otto Ambros', 'Otto Barnewald', 'Otto Bovensiepen', 'Otto Brinkmann', 'Otto Förschner', 'Otto Ohlendorf', 'Otto Ohlendorf', 'Otto Rasch', 'Otto Schulz', 'Otto Wolfgang Gunther Klaus', 'Peter Weingärtner', 'Paul Blobel', 'Paul Maischein', 'Paul Rostock', 'Peter Betz', 'Peter Merker', 'Philipp Grimm', 'Reiner Stahel', 'Richard Köhler', 'Richard Walenta', 'Rudolf Brandt', 'Rudolf Jacobi', 'Rudolf Suttrop', 'Schubert Heinz', 'Sebastian Schmid', 'Sepp Dietrich', 'Siegfried Handloser', 'Siegfried Ruff', 'Simon Wilhelm', 'Sylvester Filleboeck', 'Ulrich Greifelt', 'Viktor Brach', 'Vinzenz Schoettl', 'Vladislav Ostrovski', 'Waldemar Hoven', 'Waldemar Klingelhöfe', 'Waldemar von Radetzky', 'Walter Blume', 'Walter Buch', 'Walter Haensch', 'Walter Ulbricht', 'Walter Wendt', 'Werner Braune', 'Werner Alfred Berger', 'Werner Greunuss', 'Wilhelm Altenloh', 'Wilhelm Beiglboeck', 'Wilhelm Dorr', 'Wilhelm Pfannenstiel', 'Wilhelm Wagner', 'Wilhelm Welter', 'Willi Seibert', 'Willi Tessmann', 'Willi Zwiener', 'Wolfgang Romberg']
# Assembled from https://commons.wikimedia.org/wiki/Category:Belsen_trial_mugshots
# Note: womens names removed and added to female_guards
belsen_trial_guards = ['Ansgar Pichen', 'Erich Zoddel', 'Franz Stofel', 'Franz Xaver Trenkle', 'Ignatz Schlomovicz',
                       'Josef Kramer', 'Oscar Schmitz', 'Peter Weingärtner', 'Vladislav Ostrovski', 'Wilhelm Dorr']

# Assembled from:
# https://en.wikipedia.org/wiki/List_of_SS_personnel
# https://commons.wikimedia.org/wiki/Category:Belsen_trial_mugshots
# https://commons.wikimedia.org/wiki/Category:Mug_shots_of_Holocaust_perpetrators
# Note: womens names removed and added to female_guards
men = ['Adam Ankenbrand', 'Adam Grünewald', 'Adolf Diekmann', 'Adolf Eichmann', 'Adolf Hitler', 'Adolf Katz (SS-Mitglied)', 'Adolf Ott (SS-Mitglied)', 'Adolf Pokorny', 'Adolf Theuer', 'Adolf von Bomhard', 'Ain-Ervin Mere', 'Albert Forster', 'Albert Fredrich Schwartz', 'Albert Hartl', 'Albert Kesselring', 'Albert Konrad Gemmeker', 'Albert Widmann', 'Albin Gretsch', 'Aleksander Laak', 'Alexander Mach', 'Alexander Piorkowski', 'Alfons Rebane', 'Alfred Andreas Hofmann', 'Alfred Filbert', 'Alfred Franke-Gricksch', 'Alfred Naujocks', 'Alfred Spilker', 'Alfred Wünnenberg', 'Alfried Krupp von Bohlen', 'Alois Brunner', 'Amon Göth', 'Ansgar Pichen', 'Ante Pavelić', 'Anton Bergmeier', 'Anton Burger', 'Anton Dunckern', 'Anton Reinthaller', 'Anton Thernes', 'Anton Thumann', 'Arnold Büscher', 'Arnold Strippel', 'Arpad Wigand', 'Arthur Andrae', 'Arthur Dietzsch', 'Arthur Greiser', 'Arthur Liebehenschel', 'Arthur Mülverstedt', 'Arthur Nasse', 'Arthur Nebe', 'Arthur Rödl', 'Arthur Seyss-Inquart', 'Artur Phleps', 'August Blei', 'August Frank', 'August Heinrich Bender', 'August Heinrichsbauer', 'August Heissmeyer', 'August Hirt', 'August Miete', 'August Schmidthuber', 'Auke Bert Pattist', 'Benno Martin', 'Benno von Arent', 'Benson Railton Metcalf Freeman', 'Bernd Rosemeyer', 'Bernd von Brauchitsch', 'Bernhard Dietsche', 'Bernhard Krüger', 'Bernhard Schwarz', 'Bronislaw Kaminski', 'Bruno Beger', 'Bruno Gesche', 'Bruno Grothe', 'Bruno Lohse', 'Bruno Streckenbach', 'Carl Krauch', 'Carl Oberg', 'Carl Værnet', 'Christian Frederik von Schalburg', 'Christian Shnug', 'Christian Wirth', 'Christof Ludwig Knoll', 'Christoph Diehm', 'Christoph Graf zu Stolberg-Stolberg', 'Claus Schilling', 'Cornelius Schwanner', 'Curt von Gottberg', 'Derk-Elsko Bruins', 'Detlef Nebbe', 'Edmund Geer', 'Edmund Veesenmayer', 'Eduard Deisenhofer', 'Eduard Krebsbach', 'Eduard Lorenz', 'Eduard Paul Tratz', 'Eduard Roschmann', 'Eduard Strauch', 'Eduard Weiter', 'Eduard Wirths', 'Edward John Kerling', 'Edwin Jung', 'Edwin Katzenellenbogen', 'Eggert Reeder', 'Egon Zill', 'Emanuel Schafer', 'Emil Bühring', 'Emil Haussmann', 'Emil Mahl', 'Emil Maurice', 'Emil Mazuw', 'Emil Paul Pleissner', 'Emil Puhl', 'Emil Sembach', 'Emil Wezel', 'Enno Lolling', 'Erhard Brauny', 'Erhard Kroeger', 'Eric Muhsfeldt', 'Erich Albrecht', 'Erich Bauer', 'Erich Darre', 'Erich Deppner', 'Erich Dinges', 'Erich Ehrlinger', 'Erich Fuchs', 'Erich Hahnenbruch', 'Erich Isselhorst', 'Erich Kempka', 'Erich Klausener', 'Erich Koch', 'Erich Lachmann', 'Erich Mix', 'Erich Muhsfeldt', 'Erich Müller', 'Erich Naumann', 'Erich Neumann', 'Erich Priebke', 'Erich Schroeder', 'Erich Sparmann', 'Erich Steidtmann', 'Erich Zoddel', 'Erich von dem Bach-Zelewski', 'Erich von der Heyde', 'Ernest Peter Burger', 'Ernst-Robert Grawitz', 'Ernst August Rode', 'Ernst Barkmann', 'Ernst Biberstein', 'Ernst Boepple', 'Ernst Bürgin', 'Ernst Damzog', 'Ernst Girzick', 'Ernst Hartmann', 'Ernst Heinrich von Weizsäcker', 'Ernst Hermann Himmler', 'Ernst John von Freyend', 'Ernst Kaltenbrunner', 'Ernst Knorr', 'Ernst Korn', 'Ernst Lautz', 'Ernst Leopold Prinz zur Lippe', 'Ernst Lerch', 'Ernst Otto Fick', 'Ernst Schaefer', 'Ernst Tesseraux', 'Ernst Wilhelm Bohle', 'Ernst Woermann', 'Erwin Brandt', 'Erwin Lambert', 'Erwin Metzner', 'Erwin Rösener', 'Erwin Schulz', 'Erwin von Helmersen', 'Erwin von Lahousen', 'Eugen Dollmann', 'Eugen Steimle', 'Eugène Vaulot', 'Felix Landau', 'Felix Ruehl', 'Felix Steiner', 'Feodor Fedorenko', 'Ferdinand Porsche', 'Ferdinand von Sammern-Frankenegg', 'Franz Abromeit', 'Franz Augsberger', 'Franz Breithaupt', 'Franz Hayler', 'Franz Hössler', 'Franz Josef Huber', 'Franz Joseph, Prince of Hohenzollern-Emden', 'Franz Karl Reichleitner', 'Franz Konrad (SS officer)', 'Franz Kraus', 'Franz Kutschera', 'Franz Lenner', 'Franz Lucas', 'Franz Murer', 'Franz Rademacher', 'Franz Reichleitner', 'Franz Schädle', 'Franz Schlegelberger', 'Franz Schönhuber', 'Franz Six', 'Franz Stangl', 'Franz Stofel', 'Franz Suchomel', 'Franz Viktor Eirenschmalz', 'Franz Walter Stahlecker', 'Franz Xaver Schwarz', 'Franz Xaver Trenkle', 'Franz Ziereis', 'Franz Zinecker', 'Frederich Kritzinger', 'Frederick Duquesne', 'Fridolin Glass', 'Fridolin Puhr', 'Friedrich-Wilhelm Bock', 'Friedrich-Wilhelm Krüger', 'Friedrich Alpers', 'Friedrich Boßhammer', 'Friedrich Entress', 'Friedrich Flick', 'Friedrich Franz, Hereditary Grand Duke of Mecklenburg-Schwerin', 'Friedrich Hildebrandt', 'Friedrich Jaehne', 'Friedrich Jeckeln', 'Friedrich Panzinger', 'Friedrich Peter', 'Friedrich Ruppert', 'Friedrich Stahl', 'Friedrich Uebelhoer', 'Friedrich Weber (veterinarian)', 'Friedrich Wetzel', 'Friedrich Wilhelm', 'Fritz Arlt', 'Fritz Bartels', 'Fritz Becher', 'Fritz Buntrock', 'Fritz Darges', 'Fritz Fischer', 'Fritz Freitag', 'Fritz Gajewski', 'Fritz Grau', 'Fritz Hartjenstein', 'Fritz Henke', 'Fritz Hintermayer', 'Fritz Katzmann', 'Fritz Klein', 'Fritz Meurer', 'Fritz Popp', 'Fritz Sauckel', 'Fritz Schmelter', 'Fritz Schwalm', 'Fritz Tittmann', 'Fritz Weitzel', 'Fritz Witt', 'Fritz Wächtler', 'Fritz ter Meer', 'Fritz von Scholz', 'Gebhard Ludwig Himmler', 'Georg August Weltz', 'Georg Keppler', 'Georg Konrad Morgen', 'Georg Lörner', 'Georg Rickhey', 'Georg Ritter von Hengl', 'Georg Schnitzler', 'Georg Wilhelm Müller', 'George John Dasch', 'George Kettmann', 'Gerhard Klopfer', 'Gerhard Rose', 'Gottfried Graf von Bismarck-Schönhausen', 'Gottlieb Hering', 'Gottlob Berger', 'Gregor Ebner', 'Guenther Tesch', 'Guido Reimer', "Gunter d'Alquen", 'Gustav Abb', 'Gustav Adolf Nosske', 'Gustav Adolf Scheel', 'Gustav Adolf von Wulffen', 'Gustav Heigel', 'Gustav Laabs', 'Gustav Lombard', 'Gustav Münzberger', 'Gustav Nosske', 'Gustav Overbeck', 'Gustav Sorge', 'Gustav Wagner', 'Gustav Wilhelm Schübbe', 'Gustav von Halem', 'Günther Altenburg', 'Günther Joel', 'Günther Nebelung', 'Günther Pancke', 'Günther Schwägermann', 'Günther Tamaschke', 'Hajo Herrmann', 'Hanns Albin Rauter', 'Hanns Bobermin', 'Hanns Martin Schleyer', 'Hans-Adolf Prützmann', 'Hans-Georg von Charpentier', 'Hans-Theodor Schmidt', 'Hans Asperger', 'Hans Aumeier', 'Hans Baur', 'Hans Bavendamm', 'Hans Bothmann', 'Hans Dieter Ellenbeck', 'Hans Eisele (physician)', 'Hans F. K. Günther', 'Hans Fischböck', 'Hans Fleischhacker', 'Hans Frank', 'Hans Friedemann Götze', 'Hans Hahl', 'Hans Haltermann', 'Hans Hermann Junge', 'Hans Hinkel', 'Hans Hoffmann', 'Hans Hüttig', 'Hans Jüttner', 'Hans Kammler', 'Hans Kehrl', 'Hans Kraus', 'Hans Kugler', 'Hans Lammers', 'Hans Lörner', 'Hans Merbach', 'Hans Mueller', 'Hans Münch', 'Hans Möser', 'Hans Nieland', 'Hans Petersen', 'Hans Rinn (Bankmanager)', 'Hans Sommer', 'Hans Stark', 'Hans Tidow', 'Hans Walter Zech-Nenntwich', 'Hans Werner Aufseß', 'Hans Wilhelm König', 'Hans Woellke', 'Hans Wolf', 'Hans Wolfgang Romberg', 'Hans Zimmermann', 'Harald Kühnen', 'Harald Nugiseks', 'Harald Riipalu', 'Harold Cole', 'Hartmann Lauterbacher', 'Heinrich Buetefisch', 'Heinrich Buscher', 'Heinrich Buuck', 'Heinrich Ebersberg', 'Heinrich Emmendorfer', 'Heinrich Fehlis', 'Heinrich Freiherr von Stackelberg', 'Heinrich Gattineau', 'Heinrich Hamann (Polizist)', 'Heinrich Heim', 'Heinrich Himmler', 'Heinrich Lohl', 'Heinrich Müller', 'Heinrich Oster', 'Heinrich Petersen', 'Heinrich Schmidt', 'Heinrich Schulz (assassin)', 'Heinrich Schwarz', 'Heinrich Seetzen', 'Heinrich Sellmer', 'Heinz-Fritz Müller', 'Heinz Auerswald', 'Heinz Barth', 'Heinz Baumkötter', 'Heinz Brücher', 'Heinz Detmers', 'Heinz Fanslau', 'Heinz Felfe', 'Heinz Jost', 'Heinz Kaufmann', 'Heinz Linge', 'Heinz Linke', 'Heinz Macher', 'Heinz Reinefarth', 'Heinz Scheurlen', 'Heinz Schmid-Loßberg', 'Heinz Schubert', 'Heinz Tensfeld', 'Helge Auleb', 'Hellmuth Felmy', 'Helmut Bischoff', 'Helmut Hugo Glaser', 'Helmut Johannsen', 'Helmut Kunz', 'Helmut Kämpfe', 'Helmut Poppendick', 'Helmut Roscher', 'Helmuth Friedrichs', 'Hendrik Seyffardt', 'Henk Feldmeijer', 'Henri Fenet', 'Henri Lafont', 'Herbert Backe', 'Herbert Böttcher', 'Herbert Floss', 'Herbert Gille', 'Herbert Hans Haupt', 'Herbert Huebner', 'Herbert Kappler', 'Herbert Klemm', 'Herbert Scherpe', 'Herman Göring', 'Herman Hackman', 'Herman Helbig', 'Herman Lang', 'Hermann Abendroth', 'Hermann Becker-Freyseng', 'Hermann Boehm (eugenicist)', 'Hermann Cuhorst', 'Hermann Eberle', 'Hermann Fegelein', 'Hermann Florstedt', 'Hermann Gauch', 'Hermann Grossmann', 'Hermann Harm', 'Hermann Hartmann', 'Hermann Höfle', 'Hermann Karoli', 'Hermann Krumey', 'Hermann Maringgele', 'Hermann Michel', 'Hermann Muhs', 'Hermann Pister', 'Hermann Pook', 'Hermann Prieß', 'Hermann Schaper', 'Hermann Schmitz',
       'Hermann Weiser', 'Hilar Giebel', 'Hilmar Wäckerle', 'Hinrich Lohse', 'Hinrich Schuldt', 'Hor Wagner', 'Horst Böhme (SS officer)', 'Horst Fischer', 'Horst Klein', 'Horst Kopkow', 'Horst Schumann', 'Hubert Gomerski', 'Hubert Klausner', 'Hubert Krautwurst', 'Hugo Blaschke', 'Hugo Jury', 'Hugo Kraas', 'Hugo von Abercron', 'Humbert Achamer-Pifrader', 'Hyacinth Graf Strachwitz', 'Ignatz Schlomowicz', 'Inge Viermetz', 'Ion Antonescu', 'Irmfried Eberl', 'Jakob Grimminger', 'Jakob Sporrenberg', 'Joachim Albrecht Eggeling', 'Joachim Boosfeld', 'Joachim Entzian', 'Joachim Hamann', 'Joachim Mrugoswsky', 'Joachim Peiper', 'Joachim Ribbentrop', 'Joachim Rumohr', 'Joachim von Ribbentrop', 'Johann Beck (SS-Mitglied)', 'Johann Eichelsdoerfer', 'Johann Friedrich Stöver', 'Johann Gietler', 'Johann Kantschuster', 'Johann Kick', 'Johann Kirsch', 'Johann Klier', 'Johann Niemann', 'Johann Paul Kremer', 'Johann Rattenhuber', 'Johann Schwarzhuber', 'Johann von Leers', 'Johannes Hermann Mueller', 'Josef Albert Meisinger', 'Josef Altmeyer', 'Josef Altstötter', 'Josef Bühler', 'Josef Bürckel', 'Josef Fitzthum', 'Josef Fuchsloch', 'Josef Hirtreiter', 'Josef Kestel', 'Josef Kieffer', 'Josef Kollmer', 'Josef Kramer', 'Josef Leipold', 'Josef Mengele', 'Josef Oberhauser', 'Josef Pospichil', 'Josef Remmele', 'Josef Riegler', 'Josef Schillinger', 'Josef Spacil', 'Josef Tiso', 'Joseph Berchtold', 'Joseph Darnand', 'Joseph Klehr', 'Joseph Kramer', 'Josias, Hereditary Prince of Waldeck and Pyrmont', 'Jozef Kindel', 'Julian Scherner', 'Julius Dettmann', 'Julius Schaub', 'Julius Schreck', 'Justus Beyer', 'Jürgen Stroop', 'Jürgen Wagner', 'Jürgen von Klenck', 'Karl-Friedrich Höcker', 'Karl-Gustav Sauberzweig', 'Karl-Heinrich Brenner', 'Karl-Heinz Bendt', 'Karl-Heinz Bürger', 'Karl-Maria Demelhuber', 'Karl Babor', 'Karl Brandt', 'Karl Brunner (SS general)', 'Karl Bömelburg', 'Karl Chmielewski', 'Karl Diebitsch', 'Karl Dönitz', 'Karl Eberhard Schöngarth', 'Karl Ernst Möckel', 'Karl Fiehler', 'Karl Freiherr Michel von Tüßling', 'Karl Frenzel', 'Karl Fritzsch', 'Karl Gebhardt', 'Karl Genzken', 'Karl Gesele', 'Karl Gutenberger', 'Karl Hanke', 'Karl Hass', 'Karl Hermann Frank', 'Karl Hollidt', 'Karl Höfer', 'Karl Jäger', 'Karl Klaustermeyer', 'Karl Kloskowski', 'Karl Lange', 'Karl Maria Wiligut', 'Karl Mummenthey', 'Karl Peter Berg', 'Karl Pfeffer-Wildenbruch', 'Karl Pflaumer', 'Karl Pflomm', 'Karl Rahm', 'Karl Rasche', 'Karl Reinhardt (Politiker)', 'Karl Rühmer', 'Karl Schroeder', 'Karl Silberbauer', 'Karl Sommer (SS-Mitglied)', 'Karl Streibel', 'Karl Wilhelm Krause', 'Karl Wolff', 'Karl von Eberstein', 'Karl von Roques', 'Karlis Ozols', 'Klaus Barbie', 'Knud Børge Martinsen', 'Konrad Henlein', 'Konrad Kaletsch', 'Konrad Meyer-Hetling', 'Konrad Radunski', 'Konrad Schaefer', 'Konrad Schellong', 'Konstantin von Neurath', 'Kurt Blom', 'Kurt Bolender', 'Kurt Daluege', 'Kurt Engert', 'Kurt Franz', 'Kurt Gildisch', 'Kurt Gruber', 'Kurt Heinrich (SS-Mitglied)', 'Kurt Heissmeyer', 'Kurt Lischka', 'Kurt Mayer', 'Kurt Meyer', 'Kurt Schmidt-Klevenow', 'Kurt von Tippelskirch', 'Leo Hepp', 'Leo Petri', 'Leo Volk', 'Leonardo Conti', 'Leonhard Eichberger', 'Lorenz Hackenholt', 'Lothar Beutel', 'Lothar Fendler', 'Ludolf Jakob von Alvensleben', 'Ludolf von Alvensleben', 'Ludwig Fischer', 'Ludwig Grauert (Staatssekretär)', 'Ludwig Hahn', 'Ludwig Heinemann', 'Ludwig Kepplinger', 'Ludwig Ruckdeschel', 'Ludwig Steeg', 'Ludwig Stumpfegger', 'Léon Degrelle', 'Maria Mandel Krakow', 'Martin Bormann', 'Martin Gottfried Weiss', 'Martin Hellinger', 'Martin James Monti', 'Martin Kohlroser', 'Martin Sandberger', 'Martin Sommer', 'Martin Weiss (Nazi official)', 'Mathias Graf', 'Matthias Kleinheisterkamp', 'Max Amann', 'Max Clara', 'Max Ilgner', 'Max Jüttner', 'Max Kiefer', 'Max Koegel', 'Max Pauly', 'Max Schobert', 'Max Simon', 'Max Sollmann', 'Max Wielen', 'Max de Crinis', 'Maximilian Grabner', 'Maximilian List', 'Maximilian von Herff', 'Michael Karkoc', 'Michael Lippert', 'Michael Redwitz', 'Michael Wittmann', 'Michel Elmar', 'Odilo Globocnik', 'Oscar Hans', 'Oscar Schmitz', 'Oskar Dirlewanger', 'Oskar Gröning', 'Oskar Helbig', 'Oskar Mueller', 'Oskar Schroeder', 'Oskar Welzl', 'Oskars Dankers', 'Oswald Pohl', 'Oswald Rothaug', 'Otto-Heinrich Drechsler', 'Otto Abetz', 'Otto Abs', 'Otto Ambros', 'Otto Barnewald', 'Otto Bovensiepen', 'Otto Bradfisch', 'Otto Brinkmann', 'Otto Calliebe', 'Otto Dietrich', 'Otto Förschner', 'Otto Günsche', 'Otto Hofmann', 'Otto Moll', 'Otto Ohlendorf', 'Otto Rasch', 'Otto Schulz', 'Otto Schwarzenberger', 'Otto Skorzeny', 'Otto Steinbrinck', 'Otto Steinhäusl', 'Otto Ulm', 'Otto Wächter', 'Paul-Werner Hoppe', 'Paul Bante', 'Paul Blobel', 'Paul Dickopf', 'Paul Egger', 'Paul Fehse', 'Paul Haefliger', 'Paul Hausser', 'Paul Heigl', 'Paul Hennicke', 'Paul Maischein', 'Paul Ohler', 'Paul Otto Geibel', 'Paul Pleiger', 'Paul Radomski', 'Paul Riege', 'Paul Rostock', 'Paul Scharfe', 'Paul Scholz', 'Paul Zimmermann (SS-Mitglied)', 'Paulmann Werner', 'Perry Broad', 'Peter Betz', 'Peter Högl', 'Peter Merker', 'Peter Weingärtner', 'Philipp Bouhler', 'Philipp Grimm', 'Philipp Heinrich Hoerlein', 'Philipp Schmitt', 'Pierre Paoli', 'Pieter Menten', 'Pio Filippani Ronconi', 'Prince Christoph of Hesse', 'Professor Herbert Jankuhn', 'Reimond Tollenaere', 'Reiner Stahel', 'Reinhard Gehlen', 'Reinhard Heydrich', 'Reinhold Hanning', 'Richard Baer', 'Richard Glücks', 'Richard Hildebrandt', 'Richard Kaaserer', 'Richard Köhler', 'Richard Nitsch', 'Richard Quirin', 'Richard Schulze-Kossens', 'Richard Thomalla', 'Richard Walenta', 'Richard Walther Darré', 'Richard Wendler', 'Rochus Misch', 'Rolf Czurda', 'Rolf Engel', 'Rolf Günther', 'Rudolf August Oetker', 'Rudolf Batz', 'Rudolf Beckmann', 'Rudolf Brandt', 'Rudolf Creutz', 'Rudolf Diels', 'Rudolf Hess', 'Rudolf Höß', 'Rudolf Jacobi', 'Rudolf Kerner', 'Rudolf Lange', 'Rudolf Mildner', 'Rudolf Neugebauer', 'Rudolf Oeschey', 'Rudolf Querner', 'Rudolf Reinecke', 'Rudolf Scheide', 'Rudolf Suttrop', 'Rudolf von Ribbentrop', 'Ruediger Pipkorn', 'Samuel Kunz', 'Schubert Heinz', 'Sebastian Schmid', 'Sepp Dietrich', 'Siegfried Graetschus', 'Siegfried Handloser', 'Siegfried Ruff', 'Siegfried Seidl', 'Siegfried Wolfgang Fehmer', 'Siert Bruins', 'Sigmund Rascher', 'Sverre Riisnæs', 'Sylvester Filleböck', 'Sylvester Stadler', 'Søren Kam', 'Theodor Dannecker', 'Theodor Eicke', 'Theodor Wisch', 'Tscherim Soobzokov', 'Udo von Woyrsch', 'Uebelhack Friedrich', 'Ulrich Graf', 'Ulrich Greifelt', 'Ulrich Haberland', 'Viktor Brach', 'Viktor Eberhard Gräbner', 'Viktors Arājs', 'Vilis Janums', 'Vinzenz Kaiser', 'Vinzenz Schöttl', 'Vojtech Tuka', 'Waldemar Fegelein', 'Waldemar Hoven', 'Waldemar Klingelhöfe', 'Waldemar Kraft', 'Waldemar von Radetzky', 'Walter Blume', 'Walter Braemer', 'Walter Buch', 'Walter Dürrfeld', 'Walter Greiling', 'Walter Haensch', 'Walter Hauck', 'Walter Huppenkothen', 'Walter Koehler', 'Walter Krüger', 'Walter Kutschmann', 'Walter Laermann', 'Walter Letsch', 'Walter Quakernack', 'Walter Reder', 'Walter Schellenberg', 'Walter Schieber', 'Walter Schimana', 'Walter Schmitt', 'Walter Sohst', 'Walter Staudinger', 'Walter Ulbricht', 'Walter Warlimont', 'Walter Wendt', 'Walther Bierkamp', 'Walther Rauff Vanghøj', 'Walther Schröder', 'Werner Berger', 'Werner Best', 'Werner Blankenburg', 'Werner Braune', 'Werner Greunuss', 'Werner Haase', 'Werner Heyde', 'Werner Knab', 'Werner Lorenz', 'Werner Naumann', 'Werner Ostendorff', 'Werner Paulmann', 'Werner Thiel', 'Werner von Hoven', 'Wernher von Braun', 'Wilhelm Albert (SS officer)', 'Wilhelm Altenloh', 'Wilhelm Beiglboeck', 'Wilhelm Bittrich', 'Wilhelm Boger', 'Wilhelm Bonatz', 'Wilhelm Dörr (Nazi)', 'Wilhelm Emmerich', 'Wilhelm Friedrich Loeper', 'Wilhelm Fritz von Roettig', 'Wilhelm Fuchs', 'Wilhelm Gideon', 'Wilhelm Günther', 'Wilhelm Harster', 'Wilhelm Höttl', 'Wilhelm Karl Keppler', 'Wilhelm Kment', 'Wilhelm Koppe', 'Wilhelm Kube', 'Wilhelm Mohnke', 'Wilhelm Murr', 'Wilhelm Pfannenstiel', 'Wilhelm Rediess', 'Wilhelm Ritter von Leeb', 'Wilhelm Rosenbaum', 'Wilhelm Rudolf Mann', 'Wilhelm Schröder', 'Wilhelm Simon', 'Wilhelm Stuckart', 'Wilhelm Trabandt', 'Wilhelm Wagner', 'Wilhelm Welter', 'Wilhelm Zander', 'Wilhelm von Ammon', 'Wilhelm von Grolman', 'Wilhem Keitel', 'Willem Sassen', 'Willi Schatz', 'Willi Seibert', 'Willi Tessmann', 'Willi Zwiener', 'Willy Gerhard Hack', 'Wilmar Hager', 'Wolf-Heinrich Graf von Helldorf', 'Wolfgang Abel', 'Wolfgang Birkner', 'Wolfgang Mettgenberg', 'Wolfgang Otto (SS-Mitglied)', 'Wolfgang Romberg', 'Wolfgang Wirth', 'Wolfram Sievers', 'Władysław Ostrowski']

women = ['Alice Orlowski', 'Anna Hempel', 'Anna Klein(camp warden)', 'Anneliese Kohlmann', 'Dorothea Binz', 'Elfriede Rinkel', 'Elisabeth Becker', 'Elisabeth Lupka', 'Elisabeth Marschall', 'Elisabeth Volkenrath', 'Elsa Ehrich', 'Emma Zimmer', 'Erna Beilhardt', 'Erna Wallisch', 'Eva Justin', 'Ewa Paradies', 'Frieda Walter', 'Gerda Steinhoff', 'Gertrud Feist', 'Gertrud Saurer', 'Gertrud Scholtz-Klink', 'Greta Bösel', 'Helena Kopper', 'Hermine Braunsteiner',
         'Herta Bothe', 'Herta Oberheuser', 'Hertha Ehlert', 'Hilde Liesewitz', 'Hilde Lohbauer', 'Hildegard Kanbach', 'Hildegard Lächert', 'Hildegard Neumann', 'Ilse Forster', 'Ilse Koch', 'Ilse Lothe', 'Irene Haschke', 'Irma Grese', 'Jenny-Wanda Barkmann', 'Johanna Braach', 'Johanna Langefeld', 'Juana Bormann', 'Luise Danz', 'Margarete Gallinat', 'Maria Mandl', 'Ruth Neudeck', 'Therese Brandl', 'Vera Salvequart', 'Wanda Klaff']


current_folders = os.listdir()
current_folders.sort()
names = [name.replace('_', ' ') for name in current_folders]
