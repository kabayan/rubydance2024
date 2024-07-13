# Wow! technical background
Documentation on the creation of this video.

## Intent
- To see if it is possible to generate a critique of a work of art, rather than using it to create a work of art.
- The premise is that if the critique can be freely made by anyone who has viewed the work, it should not infringe on the artist's rights if it is made by a generative AI.
- Confirm the possibility that an AI can provide objective critiques (with limitations) that do not take into account personalities or human relationships.
- We wanted to compare the various AIs available as of July 2024 in terms of whether they could be used for critique.
- By releasing the created video as CC4.0, we wanted to be able to use it as a benchmark for comparing the critiquing performance of the generated AIs that will emerge in the future.

## License
- The videos and music are under CC 4.0
  - Please check the license of the music for commercial use.
- The program is licensed under the Apache License 2.0.

## Event Outline
- The 16th Theatre Χ International Performing Arts Festival 2024 (IDTF)
- Saturday, June 15 - Sunday, July 21, 2024
- "As Planet Earth People, Now"
    - http://www.theaterx.jp/24/240615-240721p.php
- 2024/7/13 14:30 Premiered as Rubydance "Wow!"

# Various data
## Video data
- https://www.youtube.com/watch?v=vxlv1rSnaO8
- https://github.com/kabayan/rubydance2024 (mp4)

## Source code
- Github
  - https://github.com/kabayan/rubydance2024

## Music used
- Songs from SoundCloud were used, all CC4.0.
- Note that not all songs are used in this film.
- https://soundcloud.com/wouterhoogland/animal-roadtrip?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing
- https://soundcloud.com/jean-edouard/animal-vocal-synth?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing
- https://soundcloud.com/nsnoskill/satiswaltz?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing
- https://soundcloud.com/sunshinechristo/stam?si=79959555fce647869d9435a02785946dutm_source=clipboard&utm_medium=text&utm_campaign=social_sharing
- https://soundcloud.com/lunova/lunova-labs-eplp-earth?si=256f2a0ccfec4a12afc706cbfd06c252&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

## Technology used
## Generative AI
- GPT4o(OpenAI)
  - Via Web
- Gemini Pro 1.5(Google)
  - Via Google AI Studio.
- Clude3(Anthropic)
  - Via Web
## AI related
- Text-to-Speech AI(Google)
- DeepL (Japanese-English)
## etc.
- Visual studio code, Python 3.10
- Davinci Resolve

## Build procedure
1. select music tracks and connect them
2. ask GPT4o to suggest a background color 3. give the music file to GPT4o for analysis
3. Give music files to GPT4o for analysis
   - Gemini.Clude cannot interpret the music. 4.
4. generate background video
   - Give background color information to Clude and generate program.
   - Gemini and GPT4o could not generate the program properly. 5.
5. take dance videos of each part.
6. create a short catch and critique
    - 6. generate dance video by giving it to Gemini.
    - Generated every 3 parts.
    - GPT4o and Clude3 could not generate. 7.
7. compilation of all critiques
    - Give GPT4o a summary of all three critiques together and generate a summary.
    - Gemini and Clude also generated it, but GPT4o was the most likely to do so. 8.
8. music, background video, dance video, catches, and critique were concatenated in Davinci Resolve.
