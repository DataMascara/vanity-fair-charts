/** @jsx React.DOM */

var MyContent = React.createClass({
  render: function() {
    var title = "Most mentioned luxury brands in Jay-Z's songs";
    var desc = "Recreating charts published in Vanity Fair with python!";
    return (
        <div>
            <h1>
                {title}
            </h1>
            <p>
                {desc}
            </p>
            <p>
		
            </p>
	    <p>
		Links:
		<ul>
		<li>
		<a href="http://datamascara.quora.com/Charting-Most-Mentioned-Brands-in-Jay-Zs-songs-with-Python-part-1">
		Charting Most Mentioned Brands in Jay-Z's songs with Python, part 1: Setting up the development environment and tallying word occurrences	
		</a>
		</li>
		<li>
		  <a href="https://github.com/DataMascara/vanity-fair-charts/tree/master/jayz-brands">
			Code
		  </a>
		</li>
		</ul>
	    </p>
	    <p>

	    </p>
        </div>
    );
  }
});


React.renderComponent(
  <MyContent />,
  document.getElementById('content')
);


