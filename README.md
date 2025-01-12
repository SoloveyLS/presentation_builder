# Simple presentation parser from JSON (for creating presentations with LLM)


## Installation:
Copy repo, go to the folder and run ```pip install .```

## Usage:
- Ask LLM to create a presentation on some topic (or paper) with some kind of a following command:\

==============================

I need you to prepare a presentation for {_paste you listeners description_}. It should take an {how long should it be}.
The format of your output is JSON with keys and values in format ```key : value```:
```
{
    "Slide {N}" :
    {
        "title" : {a couple of words}
        "idea" : {a couple of sentences}
        "text" : {some text to be shown at the slide - best are bullet lists, no big sheets of text at the slides}
        "formulas" : {some formulas to be shown at the slide - in LaTeX format}
        "figures": {which figures from the paper (no more then one per slide as they are quite big) or what pictures (could be more if they are small) to show at the slide}
        "speech" : {what to say during this slide - {_how many_} sentences as the presentation should take {_how long_}}
    },
}
```
{_how many_} slides.
Empty keys should contain ```null``` values.

Before that I need you to prepare a JSON with plan with following data:
```<PLAN>
"Slide {N}" : {
    "idea" : {a couple of words}
}
```
After I'll approve the plan, you'll need to start generating the presentation JSON, otherwise - improve the plan after some discussion

==============================

- paste the result into JSON
- hope for the better or correct the resulting JSON
