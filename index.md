<html>
    <body>
        <h1>Welcome to Jack's den of knowledge!</h1>
        <p>This blog seeks to record and accumulate most of my knowledge, ideas and executions, for reference, easy sharing and future retrospections. Feel free to prod around at anything! </p>
        <b>More content will soon be added - Mostly projects from the past, well documented, but also things I'm working on!</b>
        <br/>
        <h2>Latest additions:</h2>
        <ul>
  {% for post in site.posts %}
    <li>
      <h3><a href="{{site.baseurl}}{{ post.url }}">{{ post.title }}</a></h3>
      {{ post.excerpt }}
    </li>
  {% endfor %}
</ul>
    </body>
</html>
