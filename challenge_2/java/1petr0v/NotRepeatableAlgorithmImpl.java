import java.util.List;
import java.util.LinkedList;
import java.util.function.Function;
import java.util.stream.Collectors;

public class NotRepeatableAlgorithmImpl<T> implements NotRepeatableAlgorithm<T> {

    public List<T> findUniqueObjects(List<T> list) {
        List<T> output = new LinkedList();
        
        list.stream().collect(
            Collectors.groupingBy(
                Function.identity(), Collectors.counting()
            )
        ).forEach((k,v) -> {
            if(v == 1) {
                output.add(k);
            }
        });

        return output;
    }

}
