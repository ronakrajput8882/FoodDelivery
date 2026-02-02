import mongoose from'mongoose';
export const connectDB =()=>{
    mongoose.connect("mongodb+srv://ronakrajput8882:Ronak1685@cluster0.eointoz.mongodb.net/?appName=Cluster0").then(()=>{
        console.log("db connected")
    })
}
