
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="../../favicon.ico">

    <title>Simple Spelling</title>

    <!-- Bootstrap core CSS -->
    <link href="/css/bootstrap.min.css" rel="stylesheet">

    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <link href="/css/ie10-viewport-bug-workaround.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="/css/starter-template.css" rel="stylesheet">

    <!-- Just for debugging purposes. Don't actually copy these 2 lines! -->
    <!--[if lt IE 9]><script src="../../assets/js/ie8-responsive-file-warning.js"></script><![endif]-->
    <script src="/js/ie-emulation-modes-warning.js"></script>

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->

        <script  src="https://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>

        <script>
        function speak(text) {
          // Create a new instance of SpeechSynthesisUtterance.
          var msg = new SpeechSynthesisUtterance();

          // Set the text.
          msg.text = text;

          // Queue this utterance.
          speechSynthesis.speak(msg);
        }
        </script>

        <script>
        $(window).load(function() {
            setTimeout(function() { speak('{{word_speech}}');}, 100);
        });
        </script>


  </head>

  <body>

    <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="/spelling">Simple Spelling</a>
        </div>
        <div id="navbar" class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
            <li class="active"><a href="/spelling">Start Again</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>

    <div class="container" align="left">


      <div class="starter-template" align="left">

          <p class="lead"> {{progress_message}}</p>

          <div class="progress">
            <div class="progress-bar progress-bar-success progress-bar-striped" role="progressbar"
                aria-valuenow="{{correct_number}}" aria-valuemin="0" aria-valuemax="{{total_words}}" style="width:{{percent}}%">
            {{percent}}%
            </div>
          </div>

          <form action="/spell-word" method="post">
              <div class="form-group" align="left">
                <label for="guess">{{word_blanks}}</label>
                <input type="text" class="form-control" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false" autofocus id="guess" name="guess" size="10" maxlength="10"/>
              </div>
              <input value="Go!" type="submit" class="btn btn-primary"/>
              <input value="Speak" type ="button" onclick="speak('{{word_speech}}')" class="btn btn-primary"/>

          </form>
      </div>

    </div>


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="../../assets/js/vendor/jquery.min.js"><\/script>')</script>
    <script src="/js/bootstrap.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="/js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>


