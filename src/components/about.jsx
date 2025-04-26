import React from 'react'

function About() {
  return (
    <div>
        {/* <!-- about section --> */}
  <section className="about_section layout_padding2-bottom">
    <div className="container">
      <div className="row">
        <div className="col">
          <h2 className="heading_style">
            About Us
          </h2>
          <p>
            adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
            quis nostrud exercitation ullamco
          </p>
        </div>

      </div>
      <div className="row">
        <div className="col-md-6">
          <div className="about_img-box">

            <img src="images/a-truck.jpg" alt="" className="img-fluid"/>
          </div>
        </div>
        <div className="col-md-6 about_detail-container">
          <div className="about_detail-box">
            <h3>
              Company and Transport
            </h3>
            <p>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
              dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex
              ea commodo consequat. Duis aute irure dolor in reprehenderit in Lorem ipsum dolor sit amet, consectetur
              adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna as
            </p>
            <div className="d-flex  justify-content-end">
              <a href="" className="quote-btn about-btn">
                <img src="images/white-next.png" alt=""/>
                <span>
                  About More
                </span>

              </a>
            </div>
          </div>
        </div>
      </div>
    </div>

  </section>

  {/* <!-- end about section --> */}
    </div>
  )
}

export default About