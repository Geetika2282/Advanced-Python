import java.io.File;
import java.io.IOException;

public class Throw_demo {

    public static void main(String[] args) {
        try{
            File f = new File("data.txt");
            if(!f.exists())
                throw new IOException("File not present");
        }
        catch (IOException io){
            System.out.println(io.getMessage());
        }
    }
}
