<html>
    <body>
        <h1>Welcome to Jack's den of knowledge!</h1>
        <p>This blog seeks to record and accumulate most of my knowledge, ideas and executions, for reference, easy sharing and future retrospections. Feel free to prod around at anything! </p>
        
        <ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>
    </body>
</html>

