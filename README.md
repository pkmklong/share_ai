# reflect
[![<ORG_NAME>](https://circleci.com/gh/pkmklong/reflect.svg?style=shield)](https://app.circleci.com/pipelines/github/pkmklong)

POC for IOS nlp analytics

Structure/features:
* audio to text
  * AWS transcribe SDK
  * storage S3
* NLP for workclould, sentiment analysis, NER 
  * process EC2
  * libary pandas, NLTK
  * storage S3
* IOS app
  * SwiftUI

Tentative Workflow<br>
<img src="https://github.com/pkmklong/reflect/blob/master/images/reflect_flow.png" height="200"  class="center" title="Demo visualization">

TODO:
* <s>setup very basic MVP v1 with AWS S3 and AWS audio translation</s>
* <s>integrate into streamlit interface</s>
* <s>setup CI with circleci</s>
* <s>setup local deploy via docker</s>
* <s>Deploy v1 on AWS w/out transcribe services</s>
* Deploy v1 on AWS full MVP services
* refactor v1
* plan v2 specs
