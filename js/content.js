/** @jsx React.DOM */

var MyContent = React.createClass({
  render: function() {
    var title = "Vanity Fair Charts";
    var desc = "Recreate charts published in Vanity Fair with python!";
    return (
        <div>
            <h1>
                {title}
            </h1>
            <p>
                {desc}
            </p>
            <h2>
               <a href="jayz-brands/">
                Luxury brands mentioned in Jay-Z's songs
               </a>
            </h2>
            <p>

            </p>
	    <h2>
	       Popular Baby Names
	    </h2>
	    <p>

	    </p>
	    <h2>
		Color of the Year
	    </h2>
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


