//requiring packages
const express = require("express");
const bodyParser = require("body-parser");
const mongoose = require("mongoose");
const _ = require("lodash");
const app = express();

//preferences
app.set("view engine", "ejs");
app.use(express.static("public"));
app.use(bodyParser.urlencoded({ extended: true }));
mongoose.connect(
  "INSERT MONGODB URI HERE/itemsDB",
  {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  }
);

//Schemas
const itemsSchema = {
  name: String,
};
const newListSchema = {
  title: String,
  items: [itemsSchema],
};

//Models
const Item = mongoose.model("Item", itemsSchema);
const customList = mongoose.model("customList", newListSchema);

//Default items
const item1 = new Item({ name: "Hey there!" });
const item2 = new Item({
  name: "To add a new item to your list, click the + button",
});
const item3 = new Item({ name: "To delete an item, click X" });
const item4 = new Item({
  name: "To create a private list, append your password to the URL and hit ENTER",
});
const item5 = new Item({
  name: "The instructions will get wiped out automatically once you do that",
});
const defaultItems = [item1, item2, item5, item3, item4];

//Home page
app.get("/", function (req, res) {
  Item.find({}, function (err, foundItems) {
    if (foundItems.length === 0) {
      Item.insertMany(defaultItems, function (err) {
        if (err) {
          console.log(err);
        } else {
          console.log("defaultItems added to collection Items successfully!");
        }
      });
      res.redirect("/");
    } else {
      res.render("index2", { listTitle: "Today", item: foundItems });
      // console.log(res.statusCode);
    }
  });
});

app.post("/", function (request, response) {
  const kahaSeAya = request.body.list;
  if (request.body.task !== "") {
    //wipe function begins
    Item.findOneAndDelete({ name: "Hey there!" },function (err) {
      if (err) {
        console.log(err);
      }
    });
    Item.findOneAndDelete({ name: "To add a new item to your list, click the + button" },function (err) {
      if (err) {
        console.log(err);
      }
    });
    Item.findOneAndDelete({ name: "To delete an item, click X" },function (err) {
      if (err) {
        console.log(err);
      }
    });
    Item.findOneAndDelete({ name: "To create a private list, append your password to the URL and hit ENTER" },function (err) {
      if (err) {
        console.log(err);
      }
    });
    Item.findOneAndDelete({ name: "The instructions will get wiped out automatically once you do that" },function (err) {
      if (err) {
        console.log(err);
      }
    });
    //wipe function ends
    const item = new Item({ name: request.body.task });
    if (kahaSeAya === "Today") {
      
      item.save();
      response.redirect("/");
    } else {
      //wipe function begins
      customList.findOne ({ title: kahaSeAya }, function (err, foundList) {
        if (!err) {
          customList.findOneAndUpdate(
            { title: kahaSeAya },
            { $pull: { items: { name: "Hey there!" } } },
            function (err, foundList) {
              if (err) {
                console.log(err);
              }
            }
          );
          customList.findOneAndUpdate(
            { title: kahaSeAya },
            { $pull: { items: { name: "To add a new item to your list, click the + button" } } },
            function (err, foundList) {
              if (err) {
                console.log(err);
              }
            }
          );
          customList.findOneAndUpdate(
            { title: kahaSeAya },
            { $pull: { items: { name: "To delete an item, click X" } } },
            function (err, foundList) {
              if (err) {
                console.log(err);
              }
            }
          );
          customList.findOneAndUpdate(
            { title: kahaSeAya },
            { $pull: { items: { name: "To create a private list, append your password to the URL and hit ENTER" } } },
            function (err, foundList) {
              if (err) {
                console.log(err);
              }
            }
          );
          customList.findOneAndUpdate(
            { title: kahaSeAya },
            { $pull: { items: { name: "The instructions will get wiped out automatically once you do that" } } },
            function (err, foundList) {
              if (err) {
                console.log(err);
              }
            }
          );
            //wipe function 2 ends
              
          foundList.items.push(item);
          foundList.save();
          response.redirect("/" + kahaSeAya);
        } else {
          console.log(err);
        }
      });
    }
  } else {
    response.redirect("/" + kahaSeAya);
  }
});

//Delete function
app.post("/delete", function (request, response) {
  var deleteItem = request.body.checkbox;
  var listName = request.body.listName;
  if (listName === "Today") {
    Item.findByIdAndRemove(deleteItem, function (err) {
      if (err) {
        console.log(err);
      } else {
        // console.log("deleted successfully!");
      }
    });
    response.redirect("/");
  } else {
    customList.findOneAndUpdate(
      { title: listName },
      { $pull: { items: { _id: deleteItem } } },
      function (err, foundList) {
        if (!err) {
          response.redirect("/" + listName);
        }
      }
    );
  }
});

//newList
app.get("/:newList", function (req, res) {
  customList.findOne({ title: req.params.newList }, function (err, foundList) {
    if (!err) {
      if (!foundList) {
        let Title = _.capitalize(req.params.newList);
        const List1 = new customList({
          title: req.params.newList,
          items: defaultItems,
        });
        // console.log("if statement running!");
        List1.save();
        res.redirect("/" + req.params.newList);
      } else {
        res.render("index2", {
          listTitle: req.params.newList,
          item: foundList.items,
        });
        console.log(res.statusCode);
        // console.log("else statement running!");
      }
    }
  });
});

//Listen
let port = process.env.PORT;
if (port == null || port == "") {
  port = 3000;
}
app.listen(port, function () {
  console.log("The server is up and running on port:3000");
});
