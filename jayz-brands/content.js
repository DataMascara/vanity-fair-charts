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


