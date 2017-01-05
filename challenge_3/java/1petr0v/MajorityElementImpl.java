import java.util.List;
import java.util.LinkedList;
import java.util.function.Function;
import java.util.stream.Collectors;

public class MajorityElementImpl<T> implements MajorityElement<T> {

    private T instanceToReturn;

    public T findMajorObject(List<T> list) {
        instanceToReturn = null;
        list.stream().collect( //Collecting everything to map
            Collectors.groupingBy(
                Function.identity(), Collectors.counting()
            )
        ).forEach((key,value) -> {
            if(value >= list.size() / 2) {
                instanceToReturn = key;
            }
        });
        return instanceToReturn;
    }

}
