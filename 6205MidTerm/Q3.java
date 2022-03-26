
private int findIndex(T[] arr, int start, int end, T value){
        for(int i = start; i <= end; i ++){
            if(arr[i].equals(value)){
                return i;
            }
        }
        return -1;
    }

    public Node<T> getTreeFromPreOrderAndInOrder(T[] preOrder, T[] inOrder){
        Box<Integer> preIndex = new Box<>(0);

        return getTreeFromPreOrderAndInOrder(preOrder, inOrder, preIndex, 0, preOrder.length -1);
    }

    private Node<T> getTreeFromPreOrderAndInOrder(T[] preOrder, T[] inOrder, Box<Integer> preIndex, int start, int end){
        if(start > end || preIndex.data >= preOrder.length){
            return null;
        }

        Node<T> node = new Node<>(preOrder[preIndex.data]);
        preIndex.data ++;
       // System.out.println(node.data);
        int inOrderIndex = findIndex(inOrder,start, end , node.data);

        if(inOrderIndex == -1){
            node.left = null;
        }else{
            node.left = getTreeFromPreOrderAndInOrder(preOrder, inOrder, preIndex, start,inOrderIndex -1 );
        }

        if(inOrderIndex == -1){
            node.right = null;
        }else{
            node.right   = getTreeFromPreOrderAndInOrder(preOrder, inOrder, preIndex, inOrderIndex +1, end );
        }
        return node;
    }
