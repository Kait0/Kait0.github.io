from pybtex.database.input import bibtex

def get_personal_data():
    name = ["Bernhard", "Jaeger"]
    email = "bernhard.jaeger@uni-tuebingen.de"
    twitter = "bern_jaeger"
    bluesky = "bernhard-jaeger.bsky.social"
    github = "Kait0"
    linkedin = "bernhard-jaeger-289b65160"
    youtube = "@bernhard_jaeger"
    bio_text = f"""
                <p>I am a PhD student at the University of Tübingen, where I am part of the <a href="https://uni-tuebingen.de/en/fakultaeten/mathematisch-naturwissenschaftliche-fakultaet/fachbereiche/informatik/lehrstuehle/autonomous-vision/home/" target="_blank">Autonomous Vision Group </a> led by <a href="https://www.cvlibs.net/" target="_blank"> Prof. Andreas Geiger</a>. My research is supported by the <a href="https://imprs.is.mpg.de/" target="_blank"> International Max Plank Research School for Intelligent Systems</a>.
                <p>
                    <span style="font-weight: bold;">Research:</span>
                    My goal is to solve autonomous driving, which I view as an embodied intelligence problem. 
                    My research has contributed to the development of end-to-end driving technology, which by now is being widely adopted by leading industry players like Waymo, Tesla, or NVIDIA.
                    I worked on the TransFuser series of models, which is a widely used baseline in the literature. Our survey, <a href="https://ieeexplore.ieee.org/abstract/document/10614862">"End-to-end autonomous driving: Challenges and frontiers"</a> is the most cited introductory text in the field of end-to-end driving.
                    Recently I have been working on reinforcement learning (RL) techniques for training planning policies. 
                    Our method, <a href="https://arxiv.org/abs/2504.17838">CaRL</a> is the first open-source RL policy that outperformed the leading imitation learning methods on the nuPlan benchmark.
                    
                    I am committed to open contribution to the community. All my papers are freely available on arXiv, and all my code is available on GitHub. 
                    <br><br>
                    Currently, I am building a non-profit research organization to solve and open-source the science behind level 5 driving. We will be raising money and hiring people. Email me if you are interested.
                </p>
                <p>
                    <span style="font-weight: bold;">Bio:</span>
                     I studied B.Sc. Informatics: Games Engineering at the <a href="https://www.tum.de/en/" target="_blank">Technical University of Munich</a>. Following that I worked for 1 year as a software developer at <a href="https://www.ferchau.com/de/de" target="_blank">FERCHAU</a>  as graphics developer. Afterwards I did a M.Sc. in Computer Science at the <a href="https://uni-tuebingen.de/en/" target="_blank">University of Tübingen</a>. I started my PhD at the Autonomous Vision Group in April 2022.
                </p>
                <p>
                    <a href="assets/pdf/CV_Bernhard_Jaeger.pdf" target="_blank" style="margin-right: 15px"><i class="fa fa-address-card fa-lg"></i> CV</a>
                    <a href="mailto:{email}" style="margin-right: 15px"><i class="far fa-envelope-open fa-lg"></i> Mail</a>
                    <a href="https://twitter.com/{twitter}" target="_blank" style="margin-right: 15px"><i class="fab fa-twitter fa-lg"></i> Twitter</a>
                    <a href="https://bsky.app/profile/{bluesky}" target="_blank" style="margin-right: 15px"><i class="fab fa-twitter fa-lg"></i> Bluesky</a>
                    <a href="https://scholar.google.de/citations?user=JpceFvgAAAAJ&hl=en" target="_blank" style="margin-right: 15px"><i class="fa-solid fa-book"></i> Scholar</a>
                    <a href="https://github.com/{github}" target="_blank" style="margin-right: 15px"><i class="fab fa-github fa-lg"></i> Github</a>
                    <a href="https://www.linkedin.com/in/{linkedin}" target="_blank" style="margin-right: 15px"><i class="fab fa-linkedin fa-lg"></i> LinkedIn</a>
                    <a href="https://www.youtube.com/{youtube}" target="_blank" style="margin-right: 15px"><i class="fab fa-youtube fa-lg"></i> YouTube</a>
                </p>
    """
    footer = """
            <div class="col-sm-12" style="">
                <p>
                    Website template provided by  <a href="https://github.com/m-niemeyer/m-niemeyer.github.io" target="_blank">Michael Niemeyer</a>. <br>
                    <a href="https://m-niemeyer.github.io/" target="_blank">&#9883;</a>
                    <a href="https://kashyap7x.github.io/" target="_blank">&#9883;</a>
                </p>
            </div>
    """
    return name, bio_text, footer

def get_author_dict():
    return {
        'Andreas Geiger': 'https://www.cvlibs.net/',
        'Zehao Yu': 'https://niujinshuchong.github.io/',
        'Kashyap Chitta': 'https://kashyap7x.github.io/',
        'Katrin Renz': 'https://www.katrinrenz.de/',
        'Aditya Prakash': 'https://ap229997.github.io/',
        'Li Chen': 'https://www.linkedin.com/in/li-chen-30b256167/',
        'Penghao Wu': 'https://www.linkedin.com/in/penghao-wu-8b908623a/',
        'Hongyang Li': 'https://lihongyang.info/',
        'Takeru Miyato': 'https://takerum.github.io/',
        'Max Welling': 'https://staff.fnwi.uva.nl/m.welling/',
        'Daniel Dauner': 'https://danieldauner.github.io/',
        'Jens Beißwenger': 'https://www.linkedin.com/in/jens-bei%C3%9Fwenger-a82430258/',
        'Simon Gerstenecker': 'https://www.linkedin.com/in/simon-gerstenecker/',
        'Long Nguyen': 'https://ln2697.github.io/',
        'Micha Fauth': 'https://www.linkedin.com/in/micha-fauth-b4492a22b/?originalSubdomain=de',
        'Maximilian Igl': 'https://maximilianigl.com/'
        }

def generate_person_html(persons, connection=", ", make_bold=True, make_bold_name='Bernhard Jaeger', add_links=True):
    links = get_author_dict() if add_links else {}
    s = ""
    for p in persons:
        string_part_i = ""
        for name_part_i in p.get_part('first') + p.get_part('last'): 
            if string_part_i != "":
                string_part_i += " "
            string_part_i += name_part_i
        if string_part_i in links.keys():
            string_part_i = f'<a href="{links[string_part_i]}" target="_blank">{string_part_i}</a>'
        if make_bold and string_part_i == make_bold_name:
            string_part_i = f'<span style="font-weight: bold";>{make_bold_name}</span>'
        if p != persons[-1]:
            string_part_i += connection
        s += string_part_i
    return s

def get_paper_entry(entry_key, entry):
    s = """<div style="margin-bottom: 3em;"> <div class="row"><div class="col-sm-3">"""
    s += f"""<img src="{entry.fields['img']}" class="img-fluid img-thumbnail" alt="Project image">"""
    s += """</div><div class="col-sm-9">"""

    if 'award' in entry.fields.keys():
        s += f"""<a href="{entry.fields['html']}" target="_blank">{entry.fields['title']}</a> <span style="color: red;">({entry.fields['award']})</span><br>"""
    else:
        if 'html' in entry.fields.keys():
            s += f"""<a href="{entry.fields['html']}" target="_blank">{entry.fields['title']}</a> <br>"""
        else:
            s += f"""{entry.fields['title']} <br>"""

    s += f"""{generate_person_html(entry.persons['author'])} <br>"""
    if 'booktitle' in entry.fields.keys():
        s += f"""<span style="font-style: italic;">{entry.fields['booktitle']}</span>, {entry.fields['year']} <br>"""
    elif 'journal' in entry.fields.keys():
        s += f"""<span style="font-style: italic;">{entry.fields['journal']}</span>, {entry.fields['year']} <br>"""
    else:
        s += f"""<span style="font-style: italic;">{entry.fields['school']}</span>, {entry.fields['year']} <br>"""

    artefacts = {'html': 'Abs', 'pdf': 'Paper', 'supp': 'Supplemental', 'video': 'Video', 'poster': 'Poster', 'code': 'Code', 'website': 'Website'}
    i = 0
    for (k, v) in artefacts.items():
        if k in entry.fields.keys():
            if i > 0:
                s += ' / '
            s += f"""<a href="{entry.fields[k]}" target="_blank">{v}</a>"""
            i += 1

    cite = f"<pre><code>@{entry.original_type}{{" + f"{entry_key}, \n"
    cite += "\tauthor = {" + f"{generate_person_html(entry.persons['author'], make_bold=False, add_links=False, connection=' and ')}" + "}, \n"
    for entr in ['title', 'booktitle', 'year', 'school', 'journal', 'volume']:
        if entr in entry.fields.keys():
            cite += f"\t{entr} = " + "{" + f"{entry.fields[entr]}" + "}, \n"
    cite += """}</pre></code>"""
    s += " /" + f"""<button class="btn btn-link" type="button" data-toggle="collapse" data-target="#collapse{entry_key}" aria-expanded="false" aria-controls="collapseExample" style="margin-left: -6px; margin-top: -2px;">Expand bibtex</button><div class="collapse" id="collapse{entry_key}"><div class="card card-body">{cite}</div></div>"""
    s += """ </div> </div> </div>"""
    return s

def get_talk_entry(entry_key, entry):
    s = """<div style="margin-bottom: 3em;"> <div class="row"><div class="col-sm-3">"""
    s += f"""<img src="{entry.fields['img']}" class="img-fluid img-thumbnail" alt="Project image">"""
    s += """</div><div class="col-sm-9">"""
    s += f"""{entry.fields['title']}<br>"""
    s += f"""<span style="font-style: italic;">{entry.fields['booktitle']}</span>, {entry.fields['year']} <br>"""

    artefacts = {'slides': 'Slides', 'video': 'Recording'}
    i = 0
    for (k, v) in artefacts.items():
        if k in entry.fields.keys():
            if i > 0:
                s += ' / '
            s += f"""<a href="{entry.fields[k]}" target="_blank">{v}</a>"""
            i += 1
        else:
            print(f'[{entry_key}] Warning: Field {k} missing!')
    s += """ </div> </div> </div>"""
    return s

def get_publications_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file('publication_list.bib')
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s+= get_paper_entry(k, bib_data.entries[k])
    return s

def get_talks_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file('talk_list.bib')
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s+= get_talk_entry(k, bib_data.entries[k])
    return s

def get_index_html():
    pub = get_publications_html()
    talks = get_talks_html()
    name, bio_text, footer = get_personal_data()
    s = f"""
    <!doctype html>
<html lang="en">

<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css" integrity="sha512-xh6O/CkQoPOWDdYTDqeRdPCVd1SpvCA9XXcUnZS2FmJNp1coAFzvtCN9BmamE+4aHK8yyUHUSCcJHgXloTyT2A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

  <title>{name[0] + ' ' + name[1]}</title>
</head>

<body>
    <div class="container">
        <div class="row" style="margin-top: 3em;">
            <div class="col-sm-12" style="margin-bottom: 1em;">
            <h3 class="display-4" style="text-align: center;"><span style="font-weight: bold;">{name[0]}</span> {name[1]}</h3>
            </div>
            <br>
            <div class="col-md-8" style="">
                {bio_text}
            </div>
            <div class="col-md-4" style="">
                <img src="assets/img/profile.jpg" class="img-thumbnail" alt="Profile picture">
            </div>
        </div>
        <div class="row" style="margin-top: 1em;">
            <div class="col-sm-12" style="">
                <h4><b>Publications</b></h4>
                {pub}
            </div>
        </div>
        <div class="row" style="margin-top: 3em;">
            <div class="col-sm-12" style="">
                <h4><b>Talks</b></h4>
                {talks}
            </div>
        </div>
        
        <div class="row" style="margin-top: 3em;">
            <div class="col-sm-12" style="">
                <h4><b>Other activities</b></h4>
                <ul>
                <li>
                    One concern that I have as an AI researcher when publishing code is that it can potentially be used in dual-use applications. 
                    To solve this, I developed the <a href="https://civil-software-licenses.github.io/index.html", target="_blank">Civil Software Licenses</a>, which prevent dual-use of open-source software while being minimal in the restrictions they impose. 
                </li>
                <li>
                    I am a proponent of rigorous experimental evaluation in autonomous driving research and wrote a <a href="https://github.com/autonomousvision/carla_garage/blob/leaderboard_2/docs/common_mistakes_in_benchmarking_ad.md", target="_blank">guide</a> about common mistakes in the community to help people avoid common pitfalls.
                </li>
                <li>
                    The TransFuser series of models is in version 6 already. I have created a <a href="https://github.com/autonomousvision/carla_garage/blob/leaderboard_2/docs/history.md">history document</a> for people to have an easier overview.
                </li>
                </ul>
            </div>
        </div>
        
        <div class="row" style="margin-top: 3em;">
            <div class="col-sm-12" style="">
                <h4><b>News</b></h4>
                 <table>
                    <tr>
                      <td>Oct 26, 2026 &#8194;</td>
                      <td> I was selected as Top Reviewer at NeurIPS 2025.</td>
                    </tr>
                    <tr>
                       <td>Jul 01, 2025 &#8194;</td>
                       <td> The Vector Stiftung (foundation) supports my research with a grant of 91600 € for the project <br> "Skalierung von verstärkendem Lernen für Ende-zu-Ende Methoden für autonomes Fahren". <br> The grant was competitive, with a 5% acceptance rate (15/300). </td>
                     </tr>
                    <tr>
                       <td>Jun 11, 2025 &#8194;</td>
                       <td> Our team placed 2nd in the <a href="https://waymo.com/open/challenges/" target="_blank"> Waymo Vision-based End-to-End Driving Challenge </a> held at the <a href="https://cvpr2025.wad.vision/" target="_blank"> CVPR 2025 Workshop on Autonomous Driving. </a> </td>
                     </tr>
                     <tr>
                       <td>Jun 11, 2025 &#8194;</td>
                       <td> Our team placed 3rd in the <a href="https://waymo.com/open/challenges/" target="_blank"> Scenario Generation Challenge </a> held at the <a href="https://cvpr2025.wad.vision/" target="_blank"> CVPR 2025 Workshop on Autonomous Driving. </a> </td>
                     </tr>
                     <tr>
                       <td>Jun 17, 2024 &#8194;</td>
                       <td> Our team placed 2nd in the CARLA Challenge held at the CVPR 2024 Workshop <a href="https://opendrivelab.com/challenge2024/#carla" target="_blank"> Foundation Models for Autonomous Systems </a> </td>
                     </tr>
                     <tr>
                       <td>Dec 14, 2023 &#8194;</td>
                       <td> Our team placed 2nd in the CARLA Sensor Track challenge held at the <a href="https://ml4ad.github.io/" target="_blank">  Machine Learning for Autonomous Driving Symposium </a> in New Orleans. </td>
                     </tr>
                     <tr>
                       <td>Nov 21, 2022 &#8194;</td>
                       <td> Our team won the CARLA leaderboard MAP Track challenge at the NeurIPS 2022 <a href="https://ml4ad.github.io/2022/" target="_blank"> Machine Learning for Autonomous Driving </a> workshop.</td>
                     </tr>
                     <tr>
                       <td>Apr 01, 2022 </td>
                       <td> I joined the University of Tübingen as a PhD student. </td>
                     </tr>
                     <tr>
                       <td>Nov 22, 2021 </td>
                       <td> Our team placed 2nd in the NeurIPS 2021 CARLA <a href="https://ml4ad.github.io/2021/" target="_blank"> Machine Learning for Autonomous Driving </a>autonomous driving challenge </a>. </td>
                     </tr>
                </table> 
                    
            </div>
        </div>
        
        <div class="row" style="margin-top: 3em; margin-bottom: 1em;">
            {footer}
        </div>
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
      integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
      crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
      integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
      crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
      integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
      crossorigin="anonymous"></script>
</body>

</html>
    """
    return s


def write_index_html(filename='index.html'):
    s = get_index_html()
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(s)
    print(f'Written index content to {filename}.')

if __name__ == '__main__':
    write_index_html('index.html')