import React from 'react'

function Info() {
  return (
    <div>
          {/* <!-- info section --> */}
  <section className="info_section ">
    <div className="container ">
      <div className="row  mb-3 pb-4">
        <div className="col-md-3 info_logo">
          <div className="logo-box">
            <img src="images/logo-white.png" alt=""/>
            <span>
              Transportz
            </span>
          </div>
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sedconsectetur
          </p>
          <div className="info_social">
            <div>
              <a href="">
                <img src="images/fb.png" alt=""/>
              </a>
            </div>
            <div>
              <a href="">
                <img src="images/twitter.png" alt=""/>
              </a>
            </div>
            <div>
              <a href="">
                <img src="images/g-plus.png" alt=""/>
              </a>
            </div>
            <div>
              <a href="">
                <img src="images/linkedin.png" alt=""/>
              </a>
            </div>
          </div>
        </div>
        <div className="col-md-3 info_address">
          <h5>
            Address
          </h5>
          <p>
            Healing Center, 176 W Street name,
            New York, NY 10014, US
          </p>
          <p>
            (+71) 8522369417
          </p>
          <p>
            (+71) 8522369417
          </p>
          <p>
            <a href="">
              transportz@gmail.com
            </a>
          </p>
        </div>
        <div className="col-md-3 info_links">

          <div className="info_nav ">
            <nav className="">
              <ul>
                <h5>
                  Links
                </h5>
                <li>
                  <a href="index.html"> Home</a>
                </li>
                <li>
                  <a href="about.html">About</a>
                </li>
                <li>
                  <a href="service.html"> Service</a>
                </li>
                <li>
                  <a href="shop.html"> Shop</a>
                </li>
                <li>
                  <a href="company.html"> Company</a>
                </li>
                <li>
                  <a href="contact.html">Contact us</a>
                </li>

              </ul>
            </nav>
          </div>
        </div>
        <div className="col-md-3 info_news">
          <h5>
            Newsletter
          </h5>
          <form action="">
            <div>
              <input type="text" placeholder="Your Name"/>
            </div>
            <div>
              <input type="email" placeholder="Email"/>
            </div>
            <div className="d-flex justify-content-end">
              <button type="submit">
                Subscribe
              </button>
            </div>
          </form>
        </div>
      </div>


    </div>
  </section>
  {/* <!-- end info section --> */}
    </div>
  )
}

export default Info