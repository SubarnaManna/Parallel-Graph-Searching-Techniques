
import Combine from "./components/combine";
import About from "./components/about";
import Company from "./components/company";
import Contact from "./components/contact";
import Footer from "./components/footer";
import Header from "./components/header";
import Info from "./components/info";
import Index from "./components/index";
import Service from "./components/service";
import Shop from "./components/shop";
import Testimonial from "./components/testimonial";

import { BrowserRouter, Route, Switch } from 'react-router-dom';



// function App() {
//   const graph = {
//     nodes: [
//       { id: 1, label: "Node 1", title: "node 1 tootip text" },
//       { id: 2, label: "Node 2", title: "node 2 tootip text" },
//       { id: 3, label: "Node 3", title: "node 3 tootip text" },
//       { id: 4, label: "Node 4", title: "node 4 tootip text" },
//       { id: 5, label: "Node 5", title: "node 5 tootip text" }
//     ],
//     edges: [
//       { from: 1, to: 2 },
//       { from: 1, to: 3 },
//       { from: 2, to: 4 },
//       { from: 2, to: 5 }
//     ]
//   };

//   const options = {
//     layout: {
//       hierarchical: true
//     },
//     edges: {
//       color: "#000000"
//     },
//     height: "1080px"
//   };

//   const events = {
//     select: function(event) {
//       var { nodes, edges } = event;
//     }
//   };
//   return (
//     <Graph
//       graph={graph}
//       options={options}
//       events={events}
//       getNetwork={network => {
//         //  if you want access to vis.js network api you can set the state in a parent component using this property
//       }}
//     />
//   );
// }

function App(){

  return(<>
  
  <BrowserRouter>

    <Header />

    <Switch>
      <Route exact path="/" component={Combine} />
      <Route path="/about" component={About} />
      <Route path="/company" component={Company} />
      <Route path="/contact" component={Contact} />
      <Route path="/service" component={Service} />
      <Route path="/shop" component={Shop} />
      <Route path="/testimonial" component={Testimonial} />
    </Switch>

    <Testimonial/>
    <Info/>
    <Footer />

  </BrowserRouter>
  
  </>)
}

export default App;
